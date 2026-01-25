

# Day:15.01.2026
# practricing wh8ile loops


"""
Assignment 6 – Countdown (Easy)

Task:
Ask the user for a number.
Use a while loop to count down to 0 and then print "Done".

Practices:
Decrementing counters, loop termination"""




def countdown():
    print("This is a countdown game, enter a number and i will count it down to zero.")
    while True:
    
        user = int(input("Please enter a number: "))
        while user >= 0:
            print(user)
            user -= 1
        print("Done")
        break
countdown()            
            