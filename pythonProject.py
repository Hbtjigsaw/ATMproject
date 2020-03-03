#this program simulates a ATM with login and basic options
import random
users = {"ademir":"1597"}
usrpassnb = 0 

def login():
	run = 0
	key = 1
	passnb = {}
	control = []

	while run < 5:

		if not passnb:
			n1 = random.randint(0,4)
			n2 = random.randint(5,9)

			passnb[key] = n1,n2
			control.append (n1)
			control.append (n2)
			run+=1
			key+=1

		else:
			n1 = random.randint(0,4)
			if n1 in control:
				continue
			else:
				n2 = random.randint(5,9)
				if n2 in control:
					continue
				else:
					passnb[key] = n1,n2
					control.append (n1)
					control.append (n2)
					run+=1
					key+=1
	return (passnb)

def validPassnb(Passnb):

	return

#def newPassnb(opt):
	

def newUser():
	run = True
	print("Welcome "+usr.capitalize()+", you are about to open yourself a bank account")
	print("first we're going to set up your 6 digit passnumber")

	while run:
		try:
			usrpassnb = input("please enter a six-digit passnumber containing only numbers: ")
			if usrpassnb.isnumeric():
				if len(usrpassnb) == 6:
					repass = input("Please, re-enter the same passnumber to confirm or press enter to input another passnumber: ")
					if repass == usrpassnb:
						break
				
				if len(usrpassnb) > 6:
					print("The entered passnumber is greater than 6 digits, please re-enter the passnumber.")        
				
				elif len(usrpassnb) < 6:
					print("The entered passowrd is smaller than 6 digits, please re-enter the passnumber.")

			else:
				print("Use only numbers in your 6 digit passnumber!")	
		
		except:
			print("Whoops, something seems to be wrong. Please, try again")
			continue

	return (usrpassnb)

input("Welcome to your virtual bank, please press any key to login ")
usr = str(input("Please provide your first name: ")).lower()

if usr in users:
	print("Please enter your passnumber bellow",usr.capitalize())
	login()

	
else:
	run = True
	while run:
		YN = input("It looks like you still don't have set up an account, would you like to create an account now? \n(Y/N): ").lower()
		if YN == 'y' or YN == 'yes' or YN == 'sim':
			run = False
			Passnb = newUser()
		elif YN == 'n' or YN == 'no' or YN == 'nao':
			run = False
			print("exitting the program...")
		else:
			print("Please use only 'Y' to yes or 'N' to no")
	
	users[usr.lower()] = Passnb

	input()

