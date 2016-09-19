from tbay import User, Item, Bid, session 
#This part works 

'''
beyonce = User() #Creating an object named beyonce aka estantiating a class allowing you to use the properties inside the class
beyonce.username = "bknowles"
beyonce.password = "uhohuhohuhohohnana"
session.add(beyonce) #take the object and add it into session
#session.commit()
'''

#CLEAR DATABASES
users = session.query(User).all() 
items = session.query(Item).all()
bids = session.query(Bid).all()
for user in users:
    session.delete(user)
for item in items:
    session.delete(item)
for bid in bids:
    session.delete(bid)
    
session.commit()

#CREATE 3 USERS
chris = User(username = "Christopher", password = "1234")
sonia = User(username = "Sonia", password = "abcd")
alex = User(username = "Alex", password = "4567")

#CREATE 1 ITEM FOR BID
baseball = Item(name = "Mickey Mantle Signed Baseball", description = "Baseball autographed by Mickey Mantle", user=sonia)
#guitar = Item(name = "Les Paul Guitar", description = "Les Paul Guitar played by Eric Clapton", user=sonia)
#wine = Item(name = "Chateau Margaux 2009", description = "Rarest Wine in the World", user=chris)

#USERS BID ON ITEMS
chris_bid1 = Bid(price = 200, user=chris, item=baseball)
alex_bid1= Bid(price = 225, user=alex, item=baseball)
chris_bid2 = Bid(price = 230, user=chris, item=baseball)
alex_bid2 = Bid(price = 240, user=alex, item=baseball)

#need a session.add for each object
session.add_all([chris, sonia, alex, baseball, chris_bid1, alex_bid1, chris_bid2, alex_bid2])
session.commit() 

#Perform a query to find out which user placed the highest bid
bid_list = session.query(Bid.item_id, Bid.price, Bid.user_id).order_by(Bid.price.desc()).all()
user_name = session.query(User).get(bid_list[0][2])
item_name = session.query(Item).get(bid_list[0][0])

print("{0}'s bid of ${1} is currently the highest for the {2}".format(user_name.username,bid_list[0][1],item_name.name))
