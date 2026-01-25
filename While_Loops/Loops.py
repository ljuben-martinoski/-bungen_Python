"""
Practice Exercises: 
1. Print numbers 1 to 10 using while loop 
2. Print even numbers from 2 to 20 
3. Create a countdown from 10 to 1, then print "Blast off!" 
4. Sum all numbers from 1 to 100 
"""

#1. 
i = 0
while i <= 10:
    i += 1
    print(i)

print("========================================================================")

#2.
i = 0
while i <= 20:
    i += 2
    print(i)

print("========================================================================")

#3. 
i = 10
while i >= 1:
    print(i)
    i -= 1
print("Blast off!")

print("========================================================================")
#4.

sum = 0
i = 1  
while i <= 100:
    sum += i
    i += 1
print("The sum of numbers from 1 to 100 is:", sum)

"""
Assignment: Create a number guessing game: 
• Set a secret number (use a variable, we haven't learned random yet) 
• Use a while loop to keep asking for guesses 
• Tell user if their guess is too high or too low 
• When they guess correctly, print how many attempts it took 
• Add an option to quit (if they type 'quit', break the loop) 
"""



def guees_game():
    print("Hello this is a guessing game. You need to enter a number from the range 1-50 and I will tell you are you close or not!")
    set_number = 7
    user = int(input("Please enter a number:"))
    attemps = 0
    while True:
        attemps += 1
        if user < set_number:
            print("Your guess is too low!")
            user = int(input("Please enter a number:"))
        elif user > set_number:
            print("Your guess is too hight!")
            user = int(input("Please enter a number:"))
        elif user == set_number:
            print(f"Congratulations! You guessed the number in {attemps} attempts.")
            break   

guees_game()        
    


