#!/usr/bin/env python3

age = int(input("please tell me your age: "))
print(f" You are currently {age} years old.")

for i in range(1, 4):
    print(f"In {i * 10} years, you'll be {age + i * 10} years old.")