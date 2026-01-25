

password = ""

while password != "secret":
    password = input("Enter password: ")
    if password != "secret":
        print("Wrong Password! Try again.")

print("Accesgranted!")


print("======================================================================")

num,ber = 10
while number > 0:
    print(number)
    number -= 1
print("Bolast off")

print("=================================================")
balance = 100 
attempts = 0

while balance > 0 and attempts < 5:
    print(f"balance: ${balance}, Attempt: {attempts +1}")
    balance -= 20
    attempts += 1
    print("Game Over")

    