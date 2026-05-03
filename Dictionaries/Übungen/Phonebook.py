"""
Assignment — Phonebook
Build a phonebook application with a full menu loop. The phonebook stores names as keys and phone numbers as values.
Required features:

Add contact — add a new name + number (warn if name already exists)
Look up contact — search by name, show number or "not found"
Update contact — change an existing contact's number
Delete contact — remove a contact by name
List all contacts — display all contacts sorted alphabetically
Quit

Requirements:

Use a dictionary to store contacts
Handle all edge cases (looking up a name that doesn't exist, deleting a non-existent contact, etc.)
Sort the contact list when displaying
Keep running in a loop until the user quits

Stretch goals (optional):

Allow storing multiple numbers per contact (use a list as the value)
Add a search that finds partial matches (e.g., searching "lub" finds "Ljuben")
Track how many times each contact has been looked up"""


 
phonebook = {}

while True:
    print("=== 1. Add contact===")
    print("=== 2. Look up Contact===")
    print("=== 3. Update Contact===")
    print("=== 4. Delete Contact===")
    print("=== 5. List all Contacts===")
    print("=== 6. Quit===")

    choice = input("Choose an option: ")

    
    if choice == "1":
        name = input("Please enter a name: ")
        number = input("Please enter a number: ")
        if name in phonebook:
            print("Contact already exists")
        else:
            phonebook[name] = number
            print("Conntact added successfully.")

    elif choice == "2":
        name = input("Please enter a name: ")
        if name in phonebook:
            print(phonebook[name])
        else:
            print("Contact not found")

    elif choice == "3":
        name = input("Please enter a name: ")
        if name in phonebook:
            new_number = input("Please enter a new number: ")
            phonebook[name] = new_number
            print("Contact updated successfully.")
        else:
            print("contact not found.")
            
    elif choice == "4":
        name = input("Please enter a name: ")
        if name in phonebook:
            del phonebook[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found")

    elif choice == "5":
        if not phonebook:
            print("No contacts yet.")
        else:
            sorted_contacts = sorted(phonebook.items(), key=lambda x: x[0])
            for name, number in sorted_contacts:
                print(f"{name}: {number}")
    elif choice == "6":
        print("Goodbye")
        break

    else:
        print("Invalid choice. Please try again.")