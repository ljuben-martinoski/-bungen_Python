"""
User INpüut and basic Operations
"""
#Practice Exercises:

#Get two numbers from user and print all arithmetic operations on them
#Check if a number is even (use modulo)
#Calculate the area of a rectangle from user-provided length and width
#Test comparison operators with different values


print("================================================================================")

num3 = int(input("Enter a number and i will tell you is it even or not: "))
print(num3 % 2 == 0)
print("================================================================================")

lenght = int(input("Please Enter the leght of your Rectangle: "))
widht =  int(input("Please Enter the width of your Rectangle: "))

area = lenght * widht
print("The area of the rectangle is: ", area)
print("================================================================================")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Floor Division: {num1 // num2}")
print(f"Modulo: {num1 % num2}")
print(f"Exponentiation: {num1 ** num2}")


print("================================================================================")

#Assignment:
#Create a simple calculator program that:

#Asks for first number
#Asks for second number
#Prints the sum, difference, product, and quotient
#Prints whether the first number is greater than the second
#Prints the remainder when first is divided by second
#Handles the conversion from string to appropriate number type

first_num = float(input("Please Enter the first number: "))
second_num = float(input("Please Enter the second number: "))
print(f"The sum of the two numbers is: {first_num + second_num}")
print(f"The Product of your numbers is: {first_num * second_num}")
print(f"The Difference of your numbers is: {first_num - second_num}")
print(f"The Quotient of your numbers is: {first_num / second_num}")
print(first_num > second_num )

print(f"Division with a rest: {first_num % second_num}")



        

