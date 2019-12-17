#this program simulates a ATM with login and basic options
import random
users = {"ademir":"1234"}
usrpasswd = 0

def login():
    run = 0
    key = 1
    passwd = {}
    control = []

    while run < 5:

        if not passwd:
            n1 = random.randint(0,4)
            n2 = random.randint(5,9)

            passwd[key] = n1,n2
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
                    passwd[key] = n1,n2
                    control.append (n1)
                    control.append (n2)
                    run+=1
                    key+=1
    return (passwd)

def validPasswd(Passwd):

    return

def newPasswd(opt):
    opt = optTest

def newUser():
    run = True
    print("Welcome "+usr.capitalize()+", you are about to open yourself a bank account")
    print("first we're going to set up your 6 digit password")
    #username = str(input("Please enter your name: \n"))

    while run: 
        try:
            usrpasswd = input("please enter a password containing 6 numbers: ")
            if str(usrpasswd):
            
        except:
            print("Please use only numbers in your 6 digit password!")
            continue
        if len(usrpasswd) > 6:
            print("The entered password is greater than 6 digits, please re-enter the password.")        
            continue
        elif len(usrpasswd) < 6:
            print("The entered passowrd is smaller than 6 digits, please re-enter the password.")

    return (usrpasswd)

input("Welcome to your virtual bank, please press any key to login ")
usr = str(input("Please provide your first name: ")).lower()

if usr in users:
    print("Please enter your password bellow",usr.capitalize())
    login()

    validPasswd(Passwd)

else:
    run = True
    while run:
        YN = input("It looks like you still don't have set up an account, would you like to create an account now? \n(Y/N): ").lower()
        if YN == 'y' or YN == 'yes':
            run = False
            newUser()
        elif YN == 'n' or YN == 'no' or YN == 'nao':
            run = False
            print("exitting the program...")
        else:
            print("Please use only 'Y' to yes or 'N' to no")
            continue
