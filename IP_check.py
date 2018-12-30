import os #module for 'clear' command

#introduction
print("Hello this is IP checker")
print("You can write the IP adress to check")
print("or you can write a command to use:")
print("")
print("| 1) example - show the examples how to use")
print("| 2) menu - show the commands")
print("| 3) quit - to exit the program")
print("| 4) clear - to clear the screen")

#program start
while(True):

	print("")
	user_command = input("IP command:") 

	if (user_command == 'quit'):
		break #to exit the program (and break a while)
	elif (user_command == 'example'):
		print("a.b.c.d which a-d is a numbers like 192.168.1.1")
	elif (user_command == 'menu'):
		print("| 1) example - show the examples how to use")
		print("| 2) menu - show the commands")
		print("| 3) quit - close the program")
	elif (user_command == 'clear'):
		os.system('clear') # clear screen for windows and linux
	else:
		print("This is not adress or command")

def ip_check(adress):
	int(adress)
	if (adress[0:3] or adress[5:8] or adress[9:12] or adress[13:16] > 255):
		print("invalid")
	elif(adress[0:3] or adress[5:8] or adress[9:12] or adress[13:16] <= 0):
		print("invalid")
	else:
   		print("valid")

ip_check(user_command)