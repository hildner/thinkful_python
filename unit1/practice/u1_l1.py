#Actor and Role practice problem
'''
actors = {
    "Kyle MacLachlan": "Dale Cooper",
    "Sheryl Lee": "Laura Palmer",
    "Lara Flynn Boyle": "Donna Hayward",
    "Sherilyn Fenn" : "Audrey Horne"
}

for actor in actors:
  print (actor + " - " + actors[actor])
'''

#London Walkers Practice
'''
walker1 = 0
walker2 = 102
walking = True

while walking:
    if walker1 != walker2:
        walker1 += 2
        walker2 = walker2 - 1
    else:
        walking = False

print("Walkers have met at mile at mile {0}".format(walker1))
'''

phone_book = {
    "Sarah Hughes": "01234 567890",
    "Tim Taylor": "02345 678901",
    "Sam Smith":  "03456 789012"
}

'''
lookup = "Jamie Theakston"
try:
    print(phone_book[lookup])
except KeyError:
    print("Person not listed in phone book")
'''

length = 4

for i in range(length):
    print(i % length)

print(i % length)