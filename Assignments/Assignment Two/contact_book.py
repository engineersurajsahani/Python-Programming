# Contact book using dictionary
contacts = {}

def add_contact(name, number):
    contacts[name] = number

def delete_contact(name):
    if name in contacts:
        del contacts[name]

def display_contacts():
    print("Contacts:")
    for name, number in contacts.items():
        print(f"{name}: {number}")

add_contact("John", "123-456-7890")
add_contact("Alice", "987-654-3210")
display_contacts()
