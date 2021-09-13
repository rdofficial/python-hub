"""
main.py - Pattern Printer

This file contains the entire code for the pattern-printer.

Author : Rishav Das (https://github.com/rdofficial/)
Created on : October 9, 2021

Last modified by : -
Last modified on : -

Authors contributed to this script (Add your name below if you have contributed) :
1. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the required functions and modules
from sys import platform

# Checking whether color codes are supported or not
if 'linux' in platform:
	# If the platform is linux type, then we define the color code variables

	red = '\033[91m'
	green = '\033[92m'
	yellow = '\033[93m'
	blue = '\033[94m'
	red_rev = '\033[07;91m'
	defcol = '\033[00m'
else:
	# If the platform is not linux type, then we define the color code variables as empty

	red = ''
	green = ''
	yellow = ''
	blue = ''
	red_rev = ''
	defcol = ''

def increasing_order(count = 5, design = '*'):
	""" This function serves the functionality of printing patterns in increasing order. The function takes in two parameters : count, design. The count parameter determines the amount of rounds the pattern will go for, and the design will indicate the character from which the pattern is to be made of. The default value of the count is 5, and the the design is *. """

	if count == 0:
		# Making the count 1, if is specified 0 by chance

		count += 1

	for i in range(count):
		# Iterating on the count in order to create the design / pattern

		if design == '*':
			# If the design of the pattern is specified "*" by the user, then we continue

			print("*" * (i + 1))
		elif design.isnumeric():
			# If the design of the pattern is specified numeric, then we continue printing number patterns

			for j in range(i + 1):
				print(j + 1, end = ' ')
			print()
		else:
			# If the design of the pattern is something custom, then we print it whole in the design / pattern

			print(design * i)

def main():
	# Asking the user to choose a pattern design
	choice = input(f"""
Choose a design :
{yellow}1{defcol}. Increasing order pattern
{yellow}2{defcol}. Decreasing order pattern
{yellow}3{defcol}. Mixed order pattern
{yellow}0{defcol}. Exit

{blue}Enter your choice : {yellow}""")
	print(defcol, end = '')

	# Checking the user entered choice
	if choice == '0':
		# If the user enters the option for exiting the script, then we exit the execution

		exit()
	else:
		# Asking the user for the count and the design
		count = int(input(blue + 'Enter the count of pattern rounds : ' + yellow))
		design = input(blue + 'Enter the design for the pattern : ' + yellow)
		print(defcol, end = '')

		if choice == '1':
			# If the user entered choice is increasing order pattern, then we continue the task

			increasing_order(count, design)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		# If the user presses CTRL+C key combo, then we exit the execution

		exit()
	except Exception as e:
		# If there are any errors encountered during the process, then we display the error message on the console screen

		print(red_rev  + f'[ Error : {e} ]' + defcol)
		exit()
