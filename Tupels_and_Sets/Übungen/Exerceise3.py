"""Exercise 3 — Function with Tuple Return
Write a function circle_stats(radius) that returns both the area and circumference of a circle as a tuple. Unpack the result and print both values.
(Hint: area = π × r², circumference = 2 × π × r. Use import math and math.pi)"""

import math 

def circle_stats(radius):
    area = math.pi * (r ** 2)
    circumference = 2 * math.pi * radius
    return area, circumference

r = 5
area_result, circle_result = circle_stats(r)

print(f"Radius: {r}")
print(f"Area: {area_result:.2f}")
print(f"Circumference: {circle_result:.2f}")