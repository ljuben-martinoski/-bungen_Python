"""
Main Assigmnet after finishing the lists thema.
Comprehensive menagment system that tracks multiple students and their scores
"""


students = []

def add_student():
    name = input("Enter student name: ")
    if name.strip() == "":
        print("Error: Name cannot be empty!")
        return
    
    students.append([name, []]) # adding a student with a empty grade list
    print(f"Student '{name}' added successfully!")

def add_grade():
    # first cheking if are any students in the list
    if len(students) == 0:
        print("No students yet! Add a student first.")
        return
    
    
    #show all students with numbers
    print("\n=== Students ===")#
    for i in range(len(students)):
        print(f"{i+1}. {students[i][0]}") # {i+1} starting from the 1 index not the 0

    choice = input("\nEnter student number: ")




    




def view_all_students():
    if len(students) == 0:
        print("No students in the system yet!")
        return
    
    print("\n=== All Students ===")
    for i in range(len(students)):
        name = students[i][0]
        grades = students[i][1]
        print(f"{i+1}. {name}: {grades}")


def calculate_average():
    # check if grades list is empty
    if len(grades) == 0:
        return 0
    
    


def view_student_averages():
    pass


def view_statisctics():
    pass


def view_honor_roll_students():
    pass


def remove_student():
    pass


def main_menu():
    while True:
        print("\n=== Grade Management System ===")
        print("1. Add student")
        print("2. Add grade to student")
        print("3. View all students")
        print("4. View student averages")
        print("5. View class statistics")
        print("6. Exit")


        choice = input("\nEnter choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_grade()
        elif choice == "3":
            view_all_students()
        elif choice == "4":
            view_student_averages()
        elif choice == "5":
            view_statisctics()
        elif choice == "6":
            view_honor_roll_students()
        elif choice == "7":
            remove_student()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



main_menu()