print("Forked v.0.1.1")
#Lost Inspired Countdown
#Lewis N Watson

import time
import os


def start_countdown():
	os.system('cls')
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
		os.system('cls')
		start_countdown();

start_countdown();
