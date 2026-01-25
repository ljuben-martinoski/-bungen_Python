

"""
Assignment 4: Prime Number Finder 🔢
Difficulty: Hard
Write a program that:

Asks user for a number N
Finds and prints all prime numbers from 2 to N
For each number, use a while loop to check if it's prime
Count and display total primes found

Extra Challenge: Let user keep entering numbers until they type "quit"
Reminder: A prime number is only divisible by 1 and itself
"""


def primeNUmber_finder():
    print("This is a program that calculates if a number is a Prime Number!!!!")
    print("Please Enter a number and the Programm will tell you if this is a Prime Number!!!")
    while True:
        user_input = input("Please Enter a Number (or 'quit' to exit): ")
        if user_input.lower() == "quit":
            break

        try:
            n = int(user_input)
            if n < 2:
                print("Please enter a number greater than or equal to 2.\n")
                continue

            primes = []

            for num in range(2, n + 1):
                is_prime = True
                divisor = 2 #  assigning variable to start form 2 because 2 is the smallest number that could potentualy divide our number.

                # use while loop to check if num is a prime
                while divisor * divisor <= num:
                    if num % divisor == 0: # if a num is divided by divisor(which is 2), and is without rest(==).
                        is_prime = False # this means that if num is divisible by divisor(2), and has no rest(== 0),then it si not a prime number(False)
                        break
                    divisor += 1 # increment + 1

                if is_prime:
                    primes.append(num)

            print(f"Prime number from 2 to {n}: {primes}")
            print(f"Total primes found: {len(primes)}\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n") 

primeNUmber_finder()
              



















