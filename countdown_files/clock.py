import time
import os

os.system('cls')

def countdown():
	countdown_time=108
	while countdown_time >0:
		print(countdown_time - 1)
		time.sleep(1)
		time.sleep(60) #comment for 108 secs rather than 108 mins
		countdown_time -=1
	os.system('rundll32.exe user32.dll,LockWorkStation')
	os.system('taskkill /f /IM python.exe')

countdown();
