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

    students.append([name, []])  # adding a student with a empty grade list
    print(f"Student '{name}' added successfully!")


def add_grade():
    # first cheking if are any students in the list
    if len(students) == 0:
        print("No students yet! Add a student first.")
        return

    #  show all students with numbers
    print("\n=== Students ===")
    for i in range(len(students)):
        # {i+1} starting from the 1 index,not the 0.
        print(f"{i+1}. {students[i][0]}")
    try:
        choice = int(input("\nEnter student number: "))
        if 1 <= choice < len(students):
            student_index = choice - 1
            grade = float(input(f"enter grade for {students[choice][0]}: "))

            if 0 <= grade <= 100:
                # students[choice][1].append(grade)
                students[student_index][1].append(grade)
            print("Grade added. ")
        else:
            print("Error: Grade must be between 0 and 100.")
    except ValueError:
        print("Please enter a valid number.")


def view_all_students():
    if len(students) == 0:
        print("No students in the system yet!")
        return

    print("\n=== All Students ===")
    for i in range(len(students)):
        name = students[i][0]
        grades = students[i][1]
        print(f"{i+1}. {name}: {grades}")


def calculate_average(grades):
    # check if grades list is empty
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)


def view_student_averages():
    if len(students) == 0:
        print("No students in the system yet!")
        return

    print("\n=== Student Averages ===")
    for student in students:
        avg = calculate_average(student[1])
        print(f"{student[0]}: {avg:.2f}")  # ← Use 'student', not 'students[0]'


def view_statisctics():
    if not students:
        print("No data availabel.")
        return

    all_grades = []
    for student in students:
        all_grades.extend(student[1])

    if not all_grades:
        print("NO grades recorded yet.")
        return

    print("\n=== Class Statistics ===")
    print(f"Class Average: {sum(all_grades) / len(all_grades):.2f}")
    print(f"Highest Grade: {max(all_grades)}")
    print(f"Lowest Grade: {min(all_grades)}")


def view_honor_roll_students():
    print("\n=== Honor Roll Students ===")
    found = False
    for student in students:
        if calculate_average(student[1]) >= 90:
            print(f"{student[0]}")
            found = True
    if not found:
        print("No students on the honor roll yet.")


def remove_student():
    view_all_students()
    try:
        choice = int(input("Enter student number to remove: ")) - 1
        if 0 <= choice < len(students):
            removed = students.pop(choice)
            print(f"Removed {removed[0]} from the system.")
    except ValueError:
        print("Invalid input.")


def main_menu():
    while True:
        print("\n=== Grade Management System ===")
        print("1. Add student")
        print("2. Add grade to student")
        print("3. View all students")
        print("4. View student averages")
        print("5. View class statistics")
        print("6. View honor roll students")
        print("7. Remove student")
        print("8. Exit")

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
