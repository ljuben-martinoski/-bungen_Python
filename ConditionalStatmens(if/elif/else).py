"""
  Basic if statement structure and indentation 
• if-else statements 
• if-elif-else chains 
• Nested conditionals 
• Truthy and falsy values 
• Combining conditions with and, or, not 
"""


# practice 1:
# Check if a number is possitive,negative or zero

num = int(input("Please enter a number and i will tell you if is negative, possitive or zero: "))

if num > 0:
    print("Your number is bigger than Zero!")
elif num == 0:
    print("Your number is zero!")
else:
    print("Your number is a negative number!")
    
# Determine if someone can vote (age >=)

age = int(input("Please Entrer your age: "))
if age >= 18:
    print("You are eligebel to vote!")
else:
    print("You are minor and you cant vote!")

# Grade Calculator(90 + is A , 80-89 is a B, etc..)

A = int(input("Please Enter your grade and i will tell you the letter equivalent: "))

if A >= 90:
    print("You have a Grade A!")
elif A >= 80:
    print("You have a Grade B!")
elif A >= 70 :
    print("You have a Grade C!")
elif A >= 60:
    print("You have a Grade D")
elif A >= 50:
    print("Yopu have a Grade E!")
else:
    print("You didnt pass the test! Sorry")

#  Check if a year is a leap year(divisible by 4, but not 100, unless also divisible by 400)
 
year = int(input("Please enter the curen Year and i will tell you is it leao year or not: ")) # input fore the user

# checking in a if statment if the year is divisible by 4 and no rest and if is divisible by 400 with no rest, and if is divisible by 100 but with no rest,
#then we have a leap year.
if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("The year is a leap year!")
else: 
    print("The year is not a leap year!")
#

## Assigmnet: Create a program that determines ticket pricing!
#Ask for person's age
#Children (0-12): $10
#Teens (13-17): $15
#Adults (18-64): $20
#Seniors (65+): $12
#Also add a weekend surcharge of $5 (ask if it's weekend: yes/no)
#Print the final ticket price with explanation

def ticket_pricing():
    try:
        person = int(input("Please enter your age: "))
        price = 10 if person <= 12 else (15 if person <= 17 else (20 if person <= 64 else 12))
        
        weekend = input("Is it weekend? (yes/no): ").lower() == "yes"
        if weekend:
            price += 5
            print(f"Your ticket price is: ${price} (includes $5 weekend surcharge)")
        else:
            print(f"Your ticket price is: ${price}")
    
    except Exception as e:
        print("Error: " + str(e))

ticket_pricing()                      