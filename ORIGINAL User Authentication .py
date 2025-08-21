import time
import random

entry = ["yes", "no"]
user = None
while user not in entry:
    user = input("Sign up? yes/no: \n").lower()

email_id = []
age = []
password = []
id_maker = str(random.randint(32134343, 54767474))
id_num = []

def login():
    email_check = input("Enter your Email address: \n")
    while email_check not in email_id:
        print("❌❌❌❌-INCORRECT Email-❌❌❌❌")
        email_check = input("Enter your Email address: \n")
        if email_check in email_id:
            pass

    if email_check in email_id:
        pass

    password_check = input("Enter your password:\n")
    while password_check not in password:
        print("❌❌❌❌-INCORRECT PASSWORD-❌❌❌❌")
        password_check = input("Enter your password:\n")
        if password_check in password:
            pass
    if password_check in password:
        pass

    id_check = input("Enter your id:\n")
    while id_check not in id_num:
        print("❌❌❌❌-INCORRECT ID-❌❌❌❌")
        id_check = input("Enter your id again:\n")

        if id_check in id_num:
            pass
    if id_check == id_num:
        pass
    print("-----------This ACCOUNT exists-----------")
    for seconds in range(1, 0, -1):
        time.sleep(1)
        print("\n🤚🤚🤚🤚🤚🤚🤚🤚🤚🤚🤚🤚🤚🤚🤚🤚🤚🤚🤚")
        time.sleep(3)
        print("\n✅✅✅✅✅ACCESS GRANTED✅✅✅✅✅")

def register():
    Email = input("Please enter your email:\n")
    while "@" and "gmail.com" not in Email:
        print("!!!Please enter a valid email!!!")
        Email = input("Please enter your email:\n")
        if "@" and "gmail.com" in Email:
            pass

    Age = int(input("Enter your age:\n"))
    Password = input("Enter your new password:\n")
    ConfirmPassword = input("Confirm password:\n")
    email_id.append(Email)
    age.append(Age)

    while ConfirmPassword == "" or Password == "" or ConfirmPassword not in Password:
        Password = input("Enter your password again: \n")
        ConfirmPassword = input("Confirm password:\n")

    if ConfirmPassword in Password or Password != "" or ConfirmPassword != "":
        password.append(ConfirmPassword)
        for seconds in range(1, 0, -1):
            time.sleep(1)
            print("......Creating ID......")
            time.sleep(2)
            print("\nYour ID is " + id_maker)
            id_num.append(id_maker)

def displaydetails():
    print("\n✉✉✉✉✉These are your ACCOUNT details✉✉✉✉✉")
    print(f"Email: {email_id}")
    print(f"Age: {age}")
    print(f"Your ID: {id_num}")

def loginagain():
    options = ["yes"]
    player = None
    while player not in options:
        player = input("Wanna login? yes or no:\n")
        player = player.lower()
        if player == "yes":
            return True
        else:
            break

if user == "yes":
    register()
if user == "no":
    print("bye")

while loginagain():
    login()
    displaydetails()
    break

print("BRUH💀")





