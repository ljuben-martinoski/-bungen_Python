"""
Assignment:
Create a program that:

Stores your birth year in a variable
Calculates your age (use 2024 as current year)
Stores your height in meters (float)
Converts height to centimeters
Prints all information with descriptive labels
"""


def birth_year():
    birth_year = int(input("Please enter youer birth year: "))
    age = 2026 - birth_year
    hight = float(input("Please Enter your hight in feet and i will giuve it back in centimeters: "))
    convert = hight * 30.48
    print("You are ", age, "years old!")
    print("You are ", convert, " cm high!",)

birth_year()     