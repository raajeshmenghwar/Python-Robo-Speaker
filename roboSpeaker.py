#!/bin/python3

import os

# Check if this script is being run as the main program
if __name__ == '__main__':
	# Print a message to the console using asterisks for emphasis
	print('*'*50)  # This line prints a separator line
	print("Welcome to RoboSpeaker 1.1 Created by Rajesh Kumar")
	print('*'*50)  # This line prints a separator line

	# Continuously prompt the user for input until they enter 'q'
	while True:
		# Get input from the user
		x = input("Enter what you want me to speak: ")

		# If the user enters 'q', say goodbye and exit the program
		if x == "q":
			os.system("say 'bye bye friend'")
			break

		# Otherwise, use espeak to speak the user's input out loud
		command = f"espeak '{x}'"
		os.system(command)  # This line uses the os.system method to execute a command
