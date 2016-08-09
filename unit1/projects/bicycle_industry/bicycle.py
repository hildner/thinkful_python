import random

class Bicycle(object):
    product = {}
    def __init__(self,name,weight,cost,inventory):
        self.product[name] = [weight, cost, cost*1.2, inventory]

class Customer(object):
    info = {}
    def __init__(self,name,budget):
        self.info[name] = budget

class Shops(object):
    def __init__(self, models):
        print("Welcome to Python Bikes!")
        for model in models.product:
            print("We have {0} of the {1} in stock".format(models.product[model][3], model))

        
    def sell_bikes(self, models, customers, options):
        #determines who buys which bike and calculates new inventory levels and store profit
        revenue = 0
        cost = 0
        print("\nPURCHASES")
        for customer in customers.info:
            purchased = str(random.choice(options[customer]))
            budget = customers.info[customer] - models.product[purchased][2]
            print("{0} purchased a {1} for {2} leaving him/her with ${3}".format(customer, purchased, models.product[purchased][2], budget))
            revenue += models.product[purchased][2]
            cost += models.product[purchased][1]
            models.product[purchased][3] = (models.product[purchased][3] - 1)
        profit = revenue - cost
        for model in models.product:
            print("There are {} of the model {} remaining".format(models.product[model][3],model))
        print("\nThe stores profit on these sales is {}".format(profit))

def affordable_bikes(models, customers):
    '''determines what bike is in each persons price range and creates new dictionary with info'''
    affordable = {}
    for customer in customers.info:
        print("\nHello {}".format(customer))
        print("We have the following bikes under your budget of ${}".format(customers.info[customer]))
        options = []
        for model in models.product:
            if customers.info[customer] > models.product[model][2]:
                print("The {0}, which retails for ${1}".format(model, models.product[model][2]))
                options.append(model)
        affordable[customer] = options
    
    return affordable




