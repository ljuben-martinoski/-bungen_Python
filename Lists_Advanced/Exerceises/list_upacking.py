


# Use unpacking to:
# a) Get first and last items from [10, 20, 30, 40, 50]
# b) Get first item and everything else from ["a", "b", "c", "d"]
# c) Swap two variables without using a temporary variable
# d) Extract day, month, year from ["2024", "January", "15"]#


# a)

numbers = [10, 20, 30, 40, 50]
first, *_, last = numbers
print(first, last)

#b) 

letters = ["a", "b", "c", "d"]
first, *last = letters
print(first, last)

#c) 

a, b = 30, 40
a, b = b, a
print(a, b)

# d)

values = ["2024", "January", "15"]
first = values[2]
middles = values[1]
last = values[0]
print(first, middles, last)


