import json
import os


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name:<15}|{self.phone:>15}"


class PhoneBook:
    contacts_list = []
    FILE_PATH = "contacts.json"

    def __init__(self):
        self.read_file()

    def update_file(self):
        with open(self.FILE_PATH, "w") as f:
            f.write(json.dumps(self.contacts_list, default=lambda contact_obj: contact_obj.__dict__))

    def read_file(self):
        if os.path.isfile(self.FILE_PATH):
            with open(self.FILE_PATH, "r") as f:
                data = f.read().strip()
                if data:
                    self.contacts_list = json.loads(data, object_hook=lambda contact_dict: Contact(**contact_dict))
        else:
            with open(self.FILE_PATH, "w"):
                pass

    def list(self):
        print("-" * 31)
        print(f"{'Name':<15}{'Phone':>15}")
        print(*self.contacts_list, sep="\n")
        print("-" * 31)

    def search(self, name):
        for contact in self.contacts_list:
            if contact.name == name:
                return contact

    def add(self, name, phone):
        contact = self.search(name)
        if contact:
            print("Contact already exists")
        else:
            if name.isdigit() or not phone.isdigit():
                print("Wrong input")
            else:
                new_contact = Contact(name, phone)
                self.contacts_list.append(new_contact)
                self.update_file()

    def edit(self, name):
        contact = self.search(name)
        if contact:
            name = input("Enter new name\n")
            phone = input("Enter new phone\n")
            if name.isdigit() or not phone.isdigit():
                print("Wrong input")
            else:
                contact.name = name
                contact.phone = phone
                self.update_file()
        else:
            print("This contact does not exist")

    def delete(self, name):
        contact = self.search(name)
        if contact:
            print("Are you sure, you want to delete this contact?")
            print("yes/no")
            command = input()
            if command.lower() == "yes" or command.lower() == "ok":
                self.contacts_list.remove(contact)
                self.update_file()
        else:
            print("This contact does not exist")

    def find(self, name):
        contact = self.search(name)
        if contact:
            print("-" * 31)
            contact.display()
            print("-" * 31)
        else:
            print("This contact does not exist")


class Application:
    def print_menu(self):
        print("Phone book")
        print("Enter a command:")
        print(
            "list",
            "find",
            "add",
            "delete",
            "edit",
            "exit",
            sep="\n"
        )

    def enter_name(self):
        name = input("Enter a name\n>> ")
        return name

    def enter_phone(self):
        phone = input("Enter a phone number\n>> ")
        return phone

    def run(self):
        phone_book = PhoneBook()
        while True:
            self.print_menu()
            command = input(">> ")
            if command == "list":
                phone_book.list()
            elif command == "add":
                name = self.enter_name()
                phone = self.enter_phone()
                phone_book.add(name, phone)
            elif command == "delete":
                name = self.enter_name()
                phone_book.delete(name)
            elif command == "edit":
                name = self.enter_name()
                phone_book.edit(name)
            elif command == "find":
                name = self.enter_name()
                phone_book.find(name)
            elif command == "exit":
                exit(0)
            else:
                print("Wrong command")


application = Application()
application.run()
