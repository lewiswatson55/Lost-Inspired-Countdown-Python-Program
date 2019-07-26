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
	win = input("Is your OS Windows? (y/n, case-sensitive)")
	if win == "y":
		os.system('rundll32.exe user32.dll,LockWorkStation')
		os.system('taskkill /f /IM python.exe')
	else: 
		mac = input("Mac? (y/n, case-sensitive)")
		if mac == "y":
			os.system('/System/Library/CoreServices/Menu\ Extras/User.menu/Contents/Resources/CGSession -suspend')
			os.system('killall python')
		else: 
			print("Then I assume Linux")
			print("Under Construction")

countdown();
print("Forked version 0.2, thanks for using")
