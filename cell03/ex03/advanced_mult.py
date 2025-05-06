#!/usr/bin/env python3

x = 0
y = 0

while x <= 10:
    print(f"Table de {x}:", end=" ")
    while y <= 10:
        print(f"{x * y}", end=" ")
        y += 1
    y = 0
    print()
    x += 1