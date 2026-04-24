# Adding and Updating

student = {"name": "Ljuben", "grade": 95}

# adding a new key-value pair

student["email"] = "student@example.com"
student["city"] = "Skopje"

# updating an exisiting value(same syntax!)
student.update({"grade": 100, "city": "Nürnberg"})
print(student)
