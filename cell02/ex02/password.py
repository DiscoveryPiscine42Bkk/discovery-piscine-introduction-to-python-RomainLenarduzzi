#!/usr/bin/env python3

password = "Python is awesome"
user_input = str(input())

def check_password(input_password):
    if input_password == password:
          return "ACCESS GRANTED"
    else:
         return "ACCESS DENIED"
    

print(check_password(user_input))