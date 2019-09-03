#Lost Inspired Countdown
#Lewis N Watson

import time
import os


def start_countdown():
	maclin = input("Did you use start.bat? y/n, case sensitive: ")
	if maclin == "y":
		os.system('cls')
	else:
		os.system('clear')
	u_input = input(">: ")

	if str(u_input) == "4815162342":
		print("Timer Resetting...")
		time.sleep(1.5)
		os.system('start start.bat')
		os.system('taskkill /f /IM python.exe')
	elif str(u_input) == "4 8 15 16 23 42":
		print("Timer Resetting...")
		time.sleep(1.5)
		os.system('start start.bat')
		os.system('taskkill /f /IM python.exe')
		
	elif str(u_input) == "4 8 15 16 23 32":
		print("Who are you — Locke? ")
		
	elif str(u_input) == "4815162332":
		print("Who are you — Locke? ")

	else:
		if maclin == "y":
			os.system('cls')
		else: 
			os.system('clear')
		start_countdown();

start_countdown();
