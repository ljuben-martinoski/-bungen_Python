

# Day:14.01.2025
# Practicing while loops


"""
Assignment 4 – Guess the Number (Medium–Hard)

Task:
Set a secret number in the code (for example 7).
Ask the user to guess the number.
The program should:

Tell the user if the guess is too high or too low

Continue until the user guesses correctly

Requirements:

Use a while loop

Use if / elif / else

Stop only when the guess is correc"""



def guess_the_number():
    print("This is a number guessing game, you need to find the mysteryous number,\n between 0-50")
    while True:
        
        secret_number = 36
        user = int(input("Please Enter a number between 0-50: "))
        if user == secret_number:
            print("Success you got it!!!!!")
            break
        else:
            print("Try again")

guess_the_number()
