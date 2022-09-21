#!/bin/usr/env python3
number = 0
for number in range(1, 101):
    if number % 15 == 0:
        print("FizzBuzz", end=" ")
    elif number % 3 == 0:
        print("Fizz", end=" ")
    elif number % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(number, end=" ")
