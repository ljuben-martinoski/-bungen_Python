
"""Assignment 1: Number Guessing Game 🎲
Difficulty: Easy
Create a number guessing game where:

Computer picks a random number between 1-100
User has unlimited guesses
After each guess, tell them if they're too high or too low
When correct, display how many attempts it took
Use break to exit when they win"""


import random

# creating the funktion 
def number_gussing_game():
    secret_number = random.randint(1, 100) # asssigning variable to pick random number between 1-100
    attempts = 0 # assinonjg variable to count the attempts

    print("welcxome to the guessing game!!!")
    print("Im thinking of a number between 1 and 100.")
    #starting the while loop
    while True:
        guess = int(input("Enter your guess: "))  #taking user input and converting it to integer
        attempts += 1 # increasing the attempts by 1 each time user make a guess


        if guess < secret_number:   #starting the conditon to check if the guessed number is low, high or correct
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts")
            break   # stoping the loop

number_gussing_game()                




