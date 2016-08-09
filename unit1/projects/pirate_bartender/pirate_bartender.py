questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}
    
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}


def preferences():
    '''Asks the customer questions about drink preferences and compiles the answers'''
    answers = {}
    for question in questions:
        response = input(questions[question] + " (y/n)" + "\n")
        if response == 'y':
            answers[question] = True   
        elif response == 'yes':
            answers[question] = True
        else:
            answers[question] = False
         
    return answers

def make_drink():
    '''uses the customers answers to make them a drink'''
    import random
    likes = preferences()
    drinks = []
    
    for like in likes:
        if likes[like] == True:
            drinks.append(random.choice(ingredients[like]))
    
    print("\nOne drink coming up.")
    print("It's full of good stuff.  The recipe is:")
    for drink in drinks:
        print ("A {}".format(drink))
            


if __name__ == '__main__':
   make_drink()     
    
     