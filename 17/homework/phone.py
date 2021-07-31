def save_contacts():
    with open("contacts.txt", "w") as f:
        for contact in contacts:
            name, phone = contact.values()
            f.write(f"{name}, {phone}\n")


def load_contacts():
    with open("contacts.txt", "r") as f:
        deserialized_contacts = []
        for line in f.readlines():
            name, phone = line.strip().split(", ")
            deserialized_contacts.append({"name": name, "phone": phone})
        return deserialized_contacts


contacts = load_contacts()



def indent():
    print("\n")


def has_comma(name):
    if ',' in name:
        return True
    else:
        return False


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


#
#
def add(name, phone):
    contact = search(name)
    if contact in contacts:
        print("This contact already exists")
    else:
        contacts.append({"name": name, "phone": phone})
        save_contacts()


#
#
def edit(name):
    contact = search(name)
    if contact not in contacts:
        notify()
    else:
        name = input("Enter new name\n")
        phone = input("Enter new phone\n")
        if name.isdigit() or not phone.isdigit():
            print("Wrong input!")
        else:
            contact["name"] = name
            contact["phone"] = phone
            save_contacts()


def delete(name):
    contact = search(name)
    if contact not in contacts:
        notify()
    else:
        print(f"Are you sure, you want to delete contact {contact['name']}?")
        answer = input()
        if answer == "yes" or answer == "Yes" or answer == "ok" or answer == "OK":
            contacts.remove(contact)
            save_contacts()


while True:
    if contacts == []:
        print("File is empty")
        break
    else:
        contacts.sort(key=lambda person: person['name'])
        print("Enter the command you want to execute:\nlist\nfind\nadd\nedit\ndelete\nTo quit enter: exit")
        command = input()
        if command == "list":
            get_list()
        elif command == "find":
            print("Enter the name of contact you want to find")
            contact_name = input().capitalize()
            if contact_name == ' ' or contact_name == '':
                print("Wrong input!")
            else:
                find(contact_name)
        elif command == "add":
            print("Enter the name and phone number of contact you want to add")
            contact_name = input().capitalize()
            contact_phone = input()
            if contact_name == ' ' or contact_phone == ' ' or contact_name == '' or contact_phone == '':
                print("Wrong input!")
            elif contact_name.isdigit() or not contact_phone.isdigit():
                print("Wrong input!")
            elif has_comma(contact_name):
                print("Name must not contain commas")
            else:
                add(contact_name, contact_phone)
        elif command == "edit":
            print("Enter the name of contact you want to edit")
            contact_name = input()
            if contact_name == ' ' or contact_name == '':
                print("Wrong input!")
            elif has_comma(contact_name):
                print("Wrong Input!")
            else:
                edit(contact_name)
        elif command == "delete":
            print("Enter the name of contact you want to delete")
            contact_name = input()
            if contact_name == ' ' or contact_name == '':
                print("Wrong input!")
            else:
                delete(contact_name)
        elif command == "exit":
            break
        else:
            indent()
            print("There's no such command")
            indent()
