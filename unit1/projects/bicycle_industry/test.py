import random

class Bicycle(object):
    product = {}
    def __init__(self,name,weight,cost):
        self.product[self] = [name, weight, cost, cost*1.2]

class Shops(object):
    inventory = []
    def __init__(self, inventory1, inventory2):
        self.inventory = [inventory1, inventory2]
        print("Welcome to Python Bikes!")
    def sell_bikes(self, customers, options, bikes):
        for customer in customers:
            purchased = str(random.choice(options[customer[0]]))
            

class Customer(object):
    info = []
    def __init__(self,name,budget):
        self.info = [name, budget]

def affordable_bikes(bikes, customers):
    afford = {}
    for person in customers:
        print("\nHello {}".format(person[0]))
        print("We have the following bikes under your budget of ${}".format(person[1]))
        models = []
        for bike in bikes:
            if person[1]>bike[3]:
                print("The {0}, which retails for ${1}".format(bike[0], bike[3]))
                models.append([bike[0],bike[3]])
        afford[person[0]] = models
    return afford
    


shop = Shops(10,8)

model1 = Bicycle("X100",20, 100)
model2 = Bicycle("X200",15, 300)

customer1 = Customer("Alex",200)
customer2 = Customer("Beth",500)

bikes = [model1.product,model2.product]
customers = [customer1.info, customer2.info]

options = affordable_bikes(bikes,customers)
shop.sell_bikes(customers,options, bikes)


print("\n")
counter = 0
for bike in bikes:
    print("{0} - {1} uints in inventory".format(bike[0],shop.inventory[counter]))
    counter += 1
