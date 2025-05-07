#!/usr/bin/env python3

numbers = [2, 8 ,9, 48 ,8, 22, -12, 2]

print(numbers)
filtered_numbers = list(filter(lambda x : x > 5, numbers))

for i in range(len(filtered_numbers)):
        filtered_numbers[i] += 2
numbers_set = set(filtered_numbers)
print(numbers_set)