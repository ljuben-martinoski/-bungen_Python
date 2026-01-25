number = 0
while number < 10:
    number += 1
    if number & 2 == 0:
        continue
    print(number)


print("===============================================")



numbers =[5, -3, 8, -1, 10, -7, 3]
index = 0
total = 0

while index < len(numbers):
    if numbers[index] < 0:
        index += 1
        continue
    total += numbers[index]
    index += 1

print(f"Sum of the positive number: {total}")    