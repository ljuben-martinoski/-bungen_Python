


"""
Write a program that uses a while loop to print the numbers from 1 to 10, each on a new line.
"""


def counting_up():
    try:
        i = 0

        while i <= 10:
            print(i)
            i += 1
            
    except ValueError:
        print("It is the folowing error happend!!") 


counting_up()               
