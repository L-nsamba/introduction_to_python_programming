#!/usr/bin/python3

#Prompt to ask user for password
password = str(input("Please enter your password: "))

#Displays number of characters used in password
print(f"Password length: {len(password)} characters.")

#Error handling for if password contains only digits or only letters
if password.isdigit():
	print("Password type: Contains only numbers.")
	print("Access denied.")

elif password.isalpha():
	print("Password type: Contains only letters.")
	print("Access denied.")

else:
	print("Password type: Contains both letters and numbers")

	#Error handling for if the password is too short or too long
	if len(password) < 9:
		print("Access denied. Password must contain 9 characters.")

	elif len(password) > 9:
		print("Access denied. Password must contain 9 characters.")

	#Error handling for if password passes above conditions but is incorrect
	else:
		if password != "secret123":
			print("Access denied.")

		else:
			print("Access granted.")
