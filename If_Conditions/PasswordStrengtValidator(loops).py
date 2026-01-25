

"""
Create a password validator that keeps asking until password meets ALL criteria:

At least 8 characters long
Contains at least one uppercase letter
Contains at least one lowercase letter
Contains at least one digit
Contains at least one special character (!@#$%^&*)

Use continue to reject passwords that don't meet requirements and explain why.
Hint: Use string methods like .isdigit(), .isupper(), .islower()
"""


def password_validator():
    print("This is a password authecnticator!, It is designed to check your password strenght \n and to tell you if you need to improve it!!! ")
    input_password = input("Please Enter your password: ")
    # we start all as false so when can check them latter for the characters that we look for...
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for character in input_password:
        if character.isupper():
            has_upper = True

        if character.islower():
            has_lower = True

        if character.isdigit():
            has_digit = True

        if character.isalnum: # short for is alpha numeric: this method returns true when a (A-Z) or num are found in the input 
            has_special = True
    # now we are checking all conditions:
    if len(input_password) >= 12 and has_special and has_digit and has_lower and has_upper:
        print("Password is strong! ")
    else:
        print("Password is weak!")
        print("You need to add at least of the following charactrers \n A-Z, numbers and not alpha numeric characters @!§$?#...")                    
       
password_validator()
    