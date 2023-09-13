#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i >= 1:
        print(i)
        i -= 1
        print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    return [x**2 for x in int_list]

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif ((i % 5 == 0) and (i % 3 == 0)):
            print("FizzBuzz") 
        else : 
            print ("i")
    pass

# i = 0
# while i<5:
#     print("looping")
#     i += 1

# for i in range(10):
#     print("looping")
#     print(f"i is: {i}")


# player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]
# inch_heights = [height * 7920 for height in player_heights]
# player_heights = [height * 7920 for height in player_heights]
# print(player_heights)