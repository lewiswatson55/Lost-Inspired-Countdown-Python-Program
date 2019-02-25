#Lost Inspired Countdown
#Lewis N Watson

import time
import os


def start_countdown():
	os.system('cls')
	u_input = input("_> ")

	if str(u_input) == "4815162342":
		print("Timer Resetting...")
		time.sleep(2)
		os.system('start start.bat')
		os.system('taskkill /f /IM python.exe')

	else:
		os.system('cls')
		start_countdown();

start_countdown();