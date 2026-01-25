"""
Docstring for whileLoop
"""

# Example of a while loop in Python

count = 1 # setring the starting point to count

while count <= 5:
    print(f"Count is: {count}")
    count += 1  # importnant:updates the condition menas increase for one

print("loop finidhed")

## IN the next loop the condition is checked before each iteration. 
# If it's True, the loop runs. If False, the loop stops.
# this is loopü wiht user input

password =""

while password != "secret":
    password = input("Enter password: ")
    if password != "secret":
        print("Wrong password! Try again.")
print("Access granted!")

####Second example: Countdown

number = 10
while number > 0:
    print(number)
    number -= 1 # updates the condition it menas decraese for 1
print("blast off" )
# Example 3 : Multiple conditions
balance = 100
attempts = 0
while balance > 0 and attempts < 5:
    print(f"Balance: ${balance}, Attempt: {attempts + 1}")
    balance -= 20 
    attempts += 1

# counter patherns:
# Patern 1:
count = 0
while count < 5:
    print(count)
    count += 1  #increment by 1

# Pattern 2:Count Down

count = 5
while count > 0:
    print(count)
    count -= 1

#Pattern 3: Count by steps

count = 0
while count <=20:
    print(count)
    count += 5 # increment by 5(5,10,15,20)

# Pattern 4: Acumulator(Runnig total)

total = 0
number = 1
while number <=5:
    total += number
    number += 1
print(f"Sum: {total}")

#Pattern 5 Count occurences
text = "hello world"
index = 0
count_o = 0

while index < len(text):
    if text[index] == 'o':
        count_o += 1
    index += 1

print (f"Letter 'o' appears {count_o} times") 
# Sentintel values(Stopping Conditions)
# Speciel value that signals "stop the loop"
# Common sentinels:
#  -1 for numbers
#  Empty strign ""
#       





