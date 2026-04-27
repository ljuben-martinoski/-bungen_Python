# Deleting Entris
student = {"name": "obojo", "grade": 95, "city": "Skopje", "temp": "delete me"}

# del - removes the key entirely
del student["temp"]

# .pop() - remove AND returns the value

remove_grade = student.pop("grade")

print(remove_grade)
print(student)

# .pop() with default - safe if key might not exist
val = student.pop("email", "not found")
print(val)


# Clear everything 
student.clear()  # {}

