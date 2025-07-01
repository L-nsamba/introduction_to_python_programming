#!/usr/bin/python3

#Prompt for user to enter number of choice
num_one = float(input("Enter your first number: "))
num_two = float(input("Enter your second number: "))

#Prompt to enter operator of choice
operator = input("Please enter your operator of choice '[ +, -, /, *]': " " " )

#Conditions for operators
if operator == '+' :
	answer = num_one + num_two
	print(answer)
elif operator == '-' :
	answer = num_one - num_two
	print(answer)
elif operator == '*' :
	answer = num_one * num_two
	print(answer)
elif operator == '/' :
	#Error handling incase one of the numbers is zero and the other is a whole number
	if num_one == 0 or num_two == 0 :
		print("Syntax error: Unable to divide by zero.")
	else:
		answer = num_one / num_two
		answer = round(answer,4)
		print(answer)
else:
        print("Enter valid operator/number")
