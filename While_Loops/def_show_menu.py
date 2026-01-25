


def show_menu():
    try:
        print("n\--- TASK MANAGER ---")
        print("1.Add tasks")
        print("2.List tasks")
        print("3. Exit")

    except Exception as e:
        print("Es ist die folgende Fehler eingethrofen: \n" + e.args[0])


def main():
    while True:
        show_menu()
        choice = input("Choose and option (1-3): ")

        if choice == "1":
            print("Add task selected (not implemented yet)")
        elif choice == "2":
            print("List tasks selecterd (not implemented yet)")
        elif choice == "3":
            print("Exiting programn...")
            break
        else:
            print("Invalid choice, please tey again.")

main()                                 



