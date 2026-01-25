



"""
Assignment 3 – Password Check (Medium)

Task:
Set a correct password in the code (for example "python123").
Ask the user to enter the password until they get it right.
When the password is correct, print "Access granted".

Requirements:

Use a while loop

Compare strings

Do not limit the number of attempts"""


def password_checker():
    print("This is a password cheking Game,\n you need to guess for the password if you got it you win!!!")
    while True:
        
        password = "python"
        user = input("Please enter the password: ")
        if user == password:
            print("Hurray you cracked the password!!!!!!!")
            break
        if user != password:
            print("Wrong try again!!!")


password_checker()            












