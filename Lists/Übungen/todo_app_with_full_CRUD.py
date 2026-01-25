## 📝 Today's Main Assignment: Todo List Manager

# Build a **complete todo list application** with full CRUD operations (Create, Read, Update, Delete).

### Requirements:

"""Your program should:

1. **Display a menu** with these options:
   - Add a task
   - View all tasks
   - Mark task as complete (remove it)
   - Update a task
   - Exit

2. **Add tasks** - user can add new tasks to the list

3. **View tasks** - display all tasks with numbers (1, 2, 3...)

4. **Complete/Delete tasks** - user enters a number to remove that task

5. **Update tasks** - user can edit an existing task

6. **Input validation** - handle invalid menu choices and task numbers gracefully

7. **Loop continuously** until user chooses to exit """

### Sample Output:

"""=== TODO LIST MANAGER ===
1. Add task
2. View tasks
3. Complete task
4. Update task
5. Exit
Choose an option: 1

Enter new task: Buy groceries
Task added!

Choose an option: 2

Your Tasks:
1. Buy groceries
2. Finish homework
3. Call mom

Choose an option: 3
Enter task number to complete: 2
Task 'Finish homework' completed!"""


def todo_app():
    todo_list = []
    while True:
        print("===To Do Menagment App===")
        print("Menu: ")
        print("1. Add a task:")
        print("2. View all tasks:")
        print("3. Mark task as complete (remove it):")
        print("4. Update a Task:")
        print("5. Exit.")
        user = input("Choose an option: ")

        print()
        
        # the 1 option of our menu
        if user == "1":
            print("Enter new task: : ")
            b = input()
            todo_list.append(b)
            print("Task added!\n ")
        # the second optioon of our menu    
        elif user == "2":
            print("Your tasks: ")
            if len(todo_list) == 0: # the 0 tells us that the list is empty
                print("No tasks available.\n")
            else:
                for i, task in enumerate(todo_list, 1): # eumerate so we can go throught the list
                    print(f"{i}. {task}") # printing the value of i and the list
            input("\nPress Enter to return to the menu...")
            print("=====================================================\n")

        # the thisrd option of our menu         
        elif user == "3":
            print("What task want to mark as complete? ")
            # safet block
            try:
                task_num = int(input()) - 1 # using -1 to convert from user numbering to list indexing
                if 0 <= task_num < len(todo_list):  # if loop checking that the user input is not a negetive number and that it is not smaller that the lenght of the list
                    removed = todo_list.pop(task_num)
                    print(f"Task '{removed}' completed!\n")
                else:
                    print("Invalid task!!!")
            except ValueError:
                print("please enter a valid number!\n")#
        # the fourth option of the menu        
        elif user == "4":
            try:
                print("Enter a number for a task to update: ")
                task_num = int(input()) - 1 # minus 1 to convert from user numbering to list indexing(that menas that when user selects two we need to convert to index number because 2 in index numbering is actuaally 1)
                # the if statment checks that the task number is not a negative number and taht is not smaller that the lenght of the list 
                if 0 <= task_num < len(todo_list):
                    print(f"Current task: {todo_list[task_num]}") #this part actualy, replaces the old task with the new one, shows the current task so the user knows what they have updated
                    new_task = input("Enter the new task: ")
                    todo_list[task_num] = new_task
                    print("Task updated")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please Enter a valid number\n")
        elif user == "5":
            print("You are exiting the To Do app!!!")
            break
        else:
            print("Invalid option. Please try again.\n")

            
        





            

todo_app()            
