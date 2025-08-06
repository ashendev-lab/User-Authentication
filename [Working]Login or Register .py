import time
import random
#import sys


USER_name = ""


pass_word = []
id_maker = str(random.randint(32134343, 54767474))
id_num = []

def login(user_name):


    try:
        with open(f'{user_name}.txt', 'r') as file:
            Username_line = file.readline().strip()
            Email_line = file.readline().strip()
            Age_line = file.readline().strip()
            ID_line = file.readline().strip()
            Pass_line = file.readline().strip()


    # while user_name != Username_line:
    #     print("❌❌❌WRONG USERNAME❌❌❌")
    #     user_name = input("Enter your username:\n")

        email_check = input("Enter your Email address:\n")
        while email_check != Email_line:
            print("❌❌❌-INCORRECT Email-❌❌❌")
            email_check = input("Enter your Email address:\n")

        password_check = input("Enter your password:\n")
        while password_check != Pass_line:
            print("❌❌❌-INCORRECT PASSWORD-❌❌❌")
            password_check = input("Enter your password:\n")

        id_check = input("Enter your id:\n")
        while id_check != ID_line:
            print("❌❌❌-INCORRECT ID-❌❌❌")
            id_check = input("Enter your id again:\n")

        print("-----------This ACCOUNT exists-----------")
        time.sleep(2)
        print("\n✅✅✅✅✅ACCESS GRANTED✅✅✅✅✅")

    except FileNotFoundError:
        print("That username does not exist :(")
#--------------------------------------------------------------------
def register():


    Email = input("Please enter your email:\n")
    while "@" and ("gmail.com" or "outlook.com" or "hotmail.com") not in Email:
        print("!!!Please enter a valid email!!!")
        Email = input("Please enter your email:\n")
        if "@" and "gmail.com" in Email:
            pass

    Age = input("Enter your age:\n")
    while (Age.isdigit() != True):
            Age = input("Enter your age:\n")

    Password = input("Enter your new password:\n")
    while (8 >= len(Password) <= 16) or (Password.isalpha() == True) or (Password.isdigit() == True):
        print("...PLEASE ENTER A PASSWORD BETWEEN 8 TO 16 CHARACTERS [with Alphabets and Numbers]...")
        Password = input("Enter your new password:\n")


    ConfirmPassword = input("Confirm password:\n")
    while not(ConfirmPassword == Password):
        print("❌❌❌❌❌❌-Passwords do not match-❌❌❌❌❌❌")
        ConfirmPassword = input("Confirm password:\n")


    if Password == ConfirmPassword:
        pass_word.append(ConfirmPassword)
        for seconds in range(1, 0, -1):
            time.sleep(1)
            print("......Creating ID......")
            time.sleep(2)
            print("\nYour ID is " + f"{id_maker}")
            id_num.append(id_maker)
            with open(f'{USER_name}.txt', 'w') as file1:
                file1.write(f"{username}\n" + f"{Email}\n" + f"{Age}\n" + f"{id_num[0]}\n" + f"{pass_word[0]}")




#--------------------------------------------------------------------
def displaydetails(USERNAME):
    try:
        with open(f'{USERNAME}.txt') as file3:
            UserName = file3.readline().strip()
            Email = file3.readline().strip()
            Age = file3.readline().strip()
            Your_ID = file3.readline().strip()
            PASS_word = file3.readline().strip()
        print(f"Username: {UserName} \nEmail: {Email} \nYour age: {Age} \nYour ID: {Your_ID}")
    except FileNotFoundError:
        pass
#--------------------------------------------------------------------
def loginagain():
    options = ["yes"]
    player = None
    while player not in options:
        player = input("Wanna login? yes or no:\n")
        player = player.lower()
        if player == "yes":
            return True
        elif player == "no":
            break
#--------------------------------------------------------------------
# if user == "yes":
#     register()
# elif user == "no":
#     if loginagain():
#         login()
#         displaydetails()

entry = ["yes", "no"]
user = None
while user not in entry:
    user = input("Sign up? yes/no: \n").lower()


if user == "yes":
    username = input("Enter a username:\n")

    try:

        while username.isdigit() == True or username == "" or len(username) <= 4:
            username = input("Enter a username:\n")

        USER_name = username
        with open(f'{USER_name}.txt', 'x') as file:
            file.write("---Your data---")

    except FileExistsError:
        print("Username already exists — skipping creation.")
        username2 = input("Enter a username:\n")
        while username2.isdigit() == True or username2 == "" or len(username2) <= 4 or username2 == username:
            username2 = input("Enter a username:\n")

        USER_name = username2
        with open(f'{USER_name}.txt', 'w') as file:
            file.write("---Your data---")

    register()

# if user == "no":
#     USER_name = input("Ente")

while loginagain():
    USER_name = input("Enter a username: ")
    login(USER_name)
    displaydetails(USER_name)

print("Bye!")
# while loginagain():
#     login()
#     displaydetails()


