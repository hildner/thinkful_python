from bicycle import Bicycle
from bicycle import Customer
from bicycle import Shops
from bicycle import affordable_bikes


#("Model Name", weight, production cost, inventory)
models = Bicycle("X100", 20, 100, 25)
models = Bicycle("X200", 15, 300, 23)
models = Bicycle("X300", 12, 400, 21)
models = Bicycle("X400", 10, 600, 19)
models = Bicycle("X600", 8, 800, 12)


customers = Customer("Alex",200)
customers = Customer("Beth",500)
customers = Customer("Charles",1000)


shop = Shops(models)
options = affordable_bikes(models,customers)
shop.sell_bikes(models,customers,options)