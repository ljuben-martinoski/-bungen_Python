


# Function to add a new task to the task list
def add_tasks(tasks):
    # Get task name from user input
    title = input("Task name: ")
    # Append new task dictionary with title and done status (False by default)
    tasks.append({"title": title, "done":False})

# Initialize empty task list
tasks = []
# Call the add_tasks function to add a task
add_tasks(tasks)

# Function to display all tasks with their completion status
def list_tasks(tasks):
    # Loop through each task with its index
    for i, task in enumerate(tasks):
        # Show "#" if task is done, otherwise show empty space
        status = "#" if task["done"] else " "
        # Print task number, status, and title
        print(f"{i+1}. [{status}] {task['title']}")

# Call the list_tasks function to display all tasks
list_tasks(tasks)