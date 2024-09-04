contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("Contact List:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact():
    name = input("Enter the name to search: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Contact found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            return
    print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contact['phone'] = input("Enter new Phone: ")
            contact['email'] = input("Enter new Email: ")
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def contact_book():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contact_book()
