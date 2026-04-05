"""
Docstring for Lists_Advanced.Exerceises.working_with_nested_list
"""

# Given this grade data:
#grades = [
    #[85, 90, 78],  # Student 1's grades
    #[92, 88, 95],  # Student 2's grades
    #[78, 85, 80]   # Student 3's grades
#]

# Write code to:
# a) Calculate each student's average
# b) Find the highest grade overall
# c) Get all grades for test 2 (second column)
# d) Print each student's grades with their average


grades = [
    [85, 90, 78],  # Student 1's grades
    [92, 88, 95],  # Student 2's grades
    [78, 85, 80]   # Student 3's grades
]

# a)
# initiatiion a for loop, tzhat usese enumerate that gives you the index and the students grade list, 
for i, student_grades in enumerate(grades):
    average = sum(student_grades) / len(student_grades) # sum funktion adds all grades for one student, len funktion diveides bv the number of grades.
    print(f"Studen {i + 1} average: {average: .2f}")# factored string that iterates + 1 and gives the waverage with two decimal places.


# b)
highest = 0 # starting with 0as the lowest possible grade
for student_grades in grades: # loop through each students grade list
    for grade in student_grades: # loop through each individual grade
        if grade > highest: # if the grade is biger tha the value in the variable highest
            highest = grade # update highest to this new grade
print(f"Highest grade overall: {highest}")


#c) Get all grades for test 2 (second column)
test_2_grades = [] # creates a empty list so we can put the results there
for student_grades in grades: # loop through each student grade
    test_2_grades.append(student_grades[1]) # adding the grades to the new empty lsit, with the  [1] as index that menas the second grade for each studen
print(f"Test two grade: {test_2_grades}")

#d)  same as a 


