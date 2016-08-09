import sys

keep_counting = True
counter = 1

#Get number from user
if len(sys.argv) == 2:
    try:
        n = int(sys.argv[1])
    except ValueError: 
        my_input = input("Please enter a number. What number should we count to? ")
        n = int(my_input)
          
else: 
    my_input = input("What number should we count to? ")
    n = int(my_input)

#Execute Fizzbuzz Game
print("fizzbuzz counting up to {0}".format(n))
while keep_counting:
    if counter <= n:
        if counter%3 == 0:
            if counter%5 == 0:
                print("fizzbuzz")
            else:
                print("fizz")
        elif counter%5 == 0:
            print("buzz")
        else:
            print (counter)
        counter += 1
    else:
        keep_counting = False

print("Game Complete!")
