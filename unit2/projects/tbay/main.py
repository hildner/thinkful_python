from tbay import User, Item, Bid, session 
#This part works 

'''
beyonce = User() #Creating an object named beyonce aka estantiating a class allowing you to use the properties inside the class
beyonce.username = "bknowles"
beyonce.password = "uhohuhohuhohohnana"
session.add(beyonce) #take the object and add it into session
#session.commit()
'''

#Clear databases
users = session.query(User).all() 
items = session.query(Item).all()
for user in users:
    session.delete(user)
for item in items:
    session.delete(item)
    
session.commit()


#Write to database
chris = User(username = "childner", password = "1234")
sonia = User(username = "soniar", password = "abcd")
baseball = Item(name = "Mickey Mantle Signed Baseball", description = "Baseball autographed by Mickey Mantle")
guitar = Item(name = "Les Paul Guitar", description = "Les Paul Guitar played by Eric Clapton")

session.add_all([chris, baseball, sonia, guitar])
session.commit() #need a session.add for each object

x = session.query(User.username).order_by(User.username).all()
y = session.query(Item.name).order_by(Item.name).all()

print(x,"\n",y)
