

"""
Ask the user to enter numbers repeatedly.
The program should keep adding the numbers until the user enters 0.
When 0 is entered, print the total sum.
"""


def sum_until_zero():
    print("This is a game called Sum Until zero.")
    print("You can keep adding number ubntil you press 0,after you press 0,\n you will recive a sum of all the numbers that you enterd!")
    
    
    
    user_sum = 0
    
    while True:
        user = int(input("Plese Enter a number: "))
        if user == 0:
            break
        user_sum += user
        
    print(f"Total sum: {user_sum}")    

        
sum_until_zero()








