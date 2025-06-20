#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")


def square_integers(int_list):  
    squared = []
    for inte in int_list:
        square = inte ** 2
        squared.append(square)
    return squared
    

def fizzbuzz():
    for i in range(1, 101):
        if (i % 3) == 0 and (i % 5) == 0:
            print("FizzBuzz")
        elif (i % 3) == 0:
            print("Fizz")
        elif (i % 5) == 0:
            print("Buzz")
        else:
            print(i)
