#!/usr/bin/python3

#Prompt for user to enter a number
num_one = input("Enter your first number: ")
num_two = input("Enter your second number: ")
num_three = input("Enter your third number: ")

#Determination of greatest number
if int(num_one) > int(num_two) and int(num_one) > int(num_three):
	print("Number one is the greatest number")
elif int(num_two) > int(num_one) and int(num_two) > int(num_three):
	print("Number two is the greatest number")
elif int(num_three) > int(num_one) and int(num_three) > int(num_two):
	print("Number three is the greatest number")
else:
	print("Invalid number entry")

