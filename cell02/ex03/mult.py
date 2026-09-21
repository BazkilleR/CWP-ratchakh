#!/usr/bin/env python3

first_num = input("Enter the first number:\n")
second_num = input("Enter the second number:\n")
result = int(first_num) * int(second_num)

print(f"{first_num} x {second_num} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")