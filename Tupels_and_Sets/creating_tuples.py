# Creating Tuples
#  standard way
coordinates = (10, 20)
rgb_color = (255, 128, 0)
person = ("Alice", 30, "Engineer")

# without parentheses (still a tuple!)
point = 4,5
print(type(point)) # <classe 'tuple'

# single-item tuple- the comma is REQUIRED
single = (43,)   # this is a tuple
not_tuple = (42)  # this is just the integer 43

# Accessing Tuple Elements
# Exactly like lists — indexing and slicing work the same way:
person = ("Alice", 30, "Engineer")

print(person[0])   # "Alice"
print(person[-1])  # "Engineer"
print(person[1:])  #(30, 'Engineer')

# Why Immutability? The Key Insight
cordinates = (48.137, 11.576) # munich's GPS coordinates

# This will CRASH - tuples protect their data!
cordinates[0] = 99.999 # TypeError: 'tuple' object does not support item assignment
"""
Immutability is a feature, not a bug. 
We use tuples when data shouldn't change:

-GPS coordinates
-RGB colors
-Database records
-Days of the week
-Function returning multiple values
"""

# Tuple Packing and Unpacking ⭐
#  This is where tuples get really powerful:
# Packing - combining values into a tuple
point = (3, 7)

# unpacking - pulling values out into variablles
x, y = point
print(x)  # 3
print(y)  # 7

# This also works with more values:
person = ("Alice", 30, "Munich")
name, age, city = person

print(name)  # Alice
print(age)  # 30
print(city)  # Munich


# Practical magic — functions can "return multiple values" using tuples:
def get_min_max(numbers):
    return min(numbers), max(numbers)  # returns a tuple


low, high = get_min_max([4, 1, 9, 2, 7])
print(low)  # 1
print(high)  # 9

# Useful Tuple Operations 
colors = ("red", "green", "blue", "green")

len(colors)
colors.count("green")  # 2  how m any times does "green appear?"
colors.index("blue")  #  2 at what index is "blue"

"red" in colors  # True

more = colors + ("yellow",)
