#!/usr/bin/env python3

first_number = int(input("Enter the first number:\n"))
second_number = int(input("Enter the second number:\n"))
result = first_number * second_number
print(result)
print(f"{first_number} * {second_number} = {result}")

def multiply(first_number, second_number):
    if result > 0:
        return"The result is positive."
    elif result < 0:
        return "The result is negative."
    else:
        return "The result is positive and negative."
    
print(multiply(first_number, second_number))
