
# Day: 15.01.2025
# While loop übungen



"""
Assignment 5 – Menu System (Hard)

Task:
Create a menu that keeps running until the user chooses to exit.
"""
"""
1. Say Hello
2. Show numbers 1–5
3. Exit
Behavior:

If the user chooses 1, print "Hello"

If the user chooses 2, print numbers 1 to 5

If the user chooses 3, exit the program

Any other input → print "Invalid choice"

Requirements:

Use a while loop

Use if / elif / else

The loop must run until exit is selected

"""



def menu_system():
    print("\n Menu: ")
    print("\n 1. Say Hello")
    print("\n 2. Show number 1-5")
    print("\n 3. Exit")
    while True:
        user = input("\n Please choose a option in the Menu: ")
        if user == "1":
            print("Hello")
        elif user == "2":
            for i in range(1, 6):
                print(i)
        elif user == "3":
            print("Goodbye")
            break
        else:
            print("Invalid Input")


menu_system()                










