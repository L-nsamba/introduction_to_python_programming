#!/usr/bin/python3

#Prompt for user to enter two numbers and a operator of choice
number_one = float(input("Enter your first number: "))
number_two = float(input("Enter your second number: "))
operator = input("Enter an operator of choice ( +, -, *, / ): ")

#Defining the calculator function
def calculator(number_one, number_two):
    if operator == "+":
        result = number_one + number_two
        print(f"{number_one} + {number_two} = {result}" )
    elif operator == "-":
        result = number_one + number_two
        print(f"{number_one} - {number_two} = {result}" )
    elif operator == "*":
        result = number_one * number_two
        print(f"{number_one} * {number_two} = {result}" )
    elif operator == "/":
        result = number_one / number_two
        print(f"{number_one} / {number_two} = {result}" )
    else:
        print("Synatx error. Please try again!")

#Calling the calculator function
calculator (number_one, number_two)
