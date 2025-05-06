#!/usr/bin/env python3

my_number = int(input("Enter a number\n").strip())
counter = 1

while counter <= 10:
    table = my_number * counter
    print(f"{my_number} x {counter} = {table}")
    counter += 1