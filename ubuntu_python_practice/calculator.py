#!/usr/bin/python3

#Prompt for user to enter number of choice
num_one = input("Enter your first number: ")
num_two = input("Enter your second number: ")

#Prompt to enter operator of choice
operator = input("Please enter your operator of choice '[ +, -, /, *]': " " " )

#Conditions for operators
if operator == '+' :
	answer = int(num_one) + int(num_two)
	print(answer)
elif operator == '-' :
	answer = int(num_one) - int(num_two)
	print(answer)
elif operator == '*' :
	answer = int(num_one) * int(num_two)
	print(answer)
elif operator == '/' :
	#Error handling incase one of the numbers is zero and the other is a whole number
	if int(num_one) == 0 or int(num_two) == 0 :
		print("Syntax error: Unable to divide by zero.")
	else:
		answer = int(num_one) / int(num_two)
		answer = round(answer,2)
		print(answer)
else:
        print("Enter valid operator/number")
