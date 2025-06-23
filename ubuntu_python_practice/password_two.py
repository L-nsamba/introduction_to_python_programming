#!/usr/bin/python3

#Defining variables
attempts = 0
max_attempts = 3
access_granted = False

#Main loop which runs until correct password is entered
while not access_granted:
	password = str(input("Enter your password: "))

	#Stating length of password enterd
	print(f"Password length: {len(password)} characters.")

	#Error handling if password has only digits or only letters
	if password.isdigit():
		print("Password type: Contains only digits.")
	elif password.isalpha():
		print("Password type: Contains only letters.")
	else:
		print("Password type: Both letters and digits.")

	#Error handling if password is too short or too long
	if len(password) < 9:
		print("Password too short. Must contain 9 characcters.")
		attempts = attempts + 1
	elif len(password) > 9:
		print("Password too long. Must contain 9 characters.")
		attempts = attempts + 1
	else:
		#Password passed checks now checking if it is correct
		if password == "secret123":
			print("Access granted.")
			access_granted = True
		else:
			print("Access denied.")
			attempts = attempts + 1

	#Checking if user has exceeded entry limit
	if attempts >= max_attempts and not access_granted:
		print("Too many failed attempts. Terminating...")
		break
	elif attempts > 0 and not access_granted:
		remaining = max_attempts - attempts
		print(f"Warning: You have {remaining} attempts left.")

print("Program ended")
