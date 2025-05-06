#!/usr/bin/env python3

my_number = int(input("Enter a number less than 25\n").strip())

if my_number >= 25:
    print("Error")
else:
    while my_number <= 25:
        print(f"Inside the loop, my variable is {my_number}")
        my_number += 1