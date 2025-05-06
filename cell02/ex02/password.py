#!/usr/bin/env python3

password = "Python is awesome"

def check_password(input_password):
    if input_password == password:
         return "ACCESS GRANTED"
    else:
         return "ACCESS DENIED"
    
user_input = input()
print(check_password(user_input))
