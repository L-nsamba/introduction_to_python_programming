#!/usr/bin/python3

#Prompt for user to enter a number
number = int(input("Enter your number of choice: "))

#Reversing the number
reversed_number = int(str(number)[::-1])

print(f"Your number {number} reversed is {reversed_number}.")
