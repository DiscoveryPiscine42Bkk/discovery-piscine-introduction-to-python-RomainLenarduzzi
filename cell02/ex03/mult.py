#!/user/bin/env python3

first_number = int(input("Enter the first number:\n"))
second_number = int(input("Enter the second number:\n"))
print(first_number * second_number)
print(f"{first_number} * {second_number} = {first_number * second_number}")

def multiply(first_number, second_number):
    if first_number * second_number > 0:
        return"The result is positive."
    elif first_number * second_number < 0:
        return "The result is negqtive."
    else:
        return "The result is positive and negative."
    
print(multiply(first_number, second_number))
