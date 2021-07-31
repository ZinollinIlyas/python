contacts = [
    {
        "name": "John",
        "phone": "123456"
    },
    {
        "name": "Jane",
        "phone": "564321"
    },
    {
        "name": "Bob",
        "phone": "+1234"
    },
]


def indent():
    print("\n")


def notify():
    indent()
    print("Contact does not exist")
    indent()


def get_list():
    indent()
    for contact in contacts:
        print(f'{contact["name"]:8} {contact["phone"]}')
    indent()


def search(name):
    for contact in contacts:
        if name == contact["name"]:
            return contact


def find(name):
    contact = search(name)
    if contact in contacts:
        indent()
        print(f'{contact["name"]:8} {contact["phone"]}')
        indent()
    else:
        notify()


def add(name, phone):
    contact = search(name)
    if contact in contacts:
        print("This contact already exists")

    contacts.append({"name": name, "phone": phone})


def edit(name):
    contact = search(name)
    if contact not in contacts:
        notify()
    else:
        name = input("Enter new name\n")
        phone = input("Enter new phone\n")
        contact["name"] = name
        contact["phone"] = phone


def delete(name):
    contact = search(name)
    if contact not in contacts:
        notify()
    else:
        print(f"Are you sure, you want to delete contact {contact['name']}?")
        answer = input()
        if answer == "yes" or answer == "Yes" or answer == "ok" or answer == "OK":
            contacts.remove(contact)


while True:
    print("Enter the command you want to execute:\nlist\nfind\nadd\nedit\ndelete\nTo quit enter: exit")
    command = input()
    if command == "list":
        get_list()
    elif command == "find":
        print("Enter the name of contact you want to find")
        contact_name = input()
        find(contact_name)
    elif command == "add":
        print("Enter the name and phone number of contact you want to add")
        contact_name = input()
        contact_phone = input()
        add(contact_name, contact_phone)
    elif command == "edit":
        print("Enter the name of contact you want to edit")
        contact_name = input()
        edit(contact_name)
    elif command == "delete":
        print("Enter the name of contact you want to delete")
        contact_name = input()
        delete(contact_name)
    elif command == "exit":
        break
    else:
        indent()
        print("There's no such command")
        indent()
