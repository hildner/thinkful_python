import logging
import argparse
import psycopg2

# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect(database="snippets")
logging.debug("Database connection established")


def put(name, snippet):
    """
    Store a snippet with an associated name.
    """
    
    logging.info("Storing snippet {!r}: {!r}".format(name, snippet))
    try:
        with connection, connection.cursor() as cursor:
            cursor.execute("insert into snippets values (%s, %s)",(name, snippet))
    except psycopg2.IntegrityError as e:
        with connection, connection.cursor() as cursor:
            cursor.execute("update snippets set message=%s where keyword =%s",(snippet, name))
    return name, snippet

    
def get(name):
    """Retrieve the snippet with a given name.

    If there is no such snippet, return '404: Snippet Not Found'.

    Returns the snippet.
    """
    logging.info("Retrieving snippet {!r}".format(name))
    with connection, connection.cursor() as cursor:
        cursor.execute("select message from snippets where keyword=%s", (name,))
        row = cursor.fetchone()
    logging.debug("Snippet retrieved successfully.")
    if not row:
        #No snippet was found with that name.
        return "404: Snippet Not Found"
    return row[0]

def catalog():
    print("List of keywords:")
    logging.info("Retrieving list of keywords")
    with connection, connection.cursor() as cursor:
        cursor.execute("select keyword from snippets order by keyword")
        keywords = cursor.fetchall()
    return keywords

def search(term):
    print("The following snippets contain the word '{}'".format(term))
    logging.info("Retrieving list of keywords")
    with connection, connection.cursor() as cursor:
        cursor.execute("select * from snippets where message like '%{}%'".format(term))
        matches = cursor.fetchall()
    return matches
    

def main():
    """Main Function"""
    logging.info("Constructing Parser")
    parser = argparse.ArgumentParser(description="Store and revive snippets of text")
    subparsers = parser.add_subparsers(dest="command", help="Available Commands")
    
    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="Name of the snippet")
    put_parser.add_argument("snippet", help="Snippet text")  
    
    # Subparser for the get command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help="Revive a snippet")
    get_parser.add_argument("name", help="Name of the snippet")
    
     # Subparser for the catalog command
    logging.debug("Constructing catalog subparser")
    catalog_parser = subparsers.add_parser("catalog", help="Reveal list of keywords")
    
     # Subparser for the search command
    logging.debug("Constructing search subparser")
    search_parser = subparsers.add_parser("search", help="Find snippets containing search term")
    search_parser.add_argument("term", help="Word you are searching for in existing snippets")
    
    arguments = parser.parse_args()
    
    #Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")
    
    if command == "put":
        name, snippet = put(**arguments)
        print("Stored {!r} as {!r}".format(snippet,name))
    elif command == "get":
        snippet = get(**arguments)
        print("Retrieved snippet: {!r}".format(snippet))
    elif command == "catalog":
        keywords = catalog(**arguments)
        for keyword in keywords:
            print(keyword)
    elif command == "search":
        matches = search(**arguments)
        for match in matches:
            print(match)


if __name__ == "__main__":
    main()