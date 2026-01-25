"""
Docstring for Lists.slicing
"""


# Wichtig!!!!

# Syntax : list[start:stop:step]
#       number=[1:2:6]
# start: where to begin the sleicing
# stop: where to end
# step: how many to skip(defaults is 1)

#### example

numbers = [1,2,3,4,5,6,7,8,9,]
print(numbers[2:6]) # prints then itrems starting from the 3 item.
print(numbers[1:3:9]) # start at the first 
print(numbers[::2])   # every second element 
print(numbers[:7:2]) # up to the number 7 every second element 
print(numbers[:5])  # alle numer bis 5
print(numbers[7:]) # die letzte zwei
print(numbers[::-1]) # reversed 
print(numbers[0:9]) # start at the first end at the last