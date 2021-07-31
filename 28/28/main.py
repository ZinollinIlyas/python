import mysql.connector
from datetime import date
import sys


class Admin:
    connection = mysql.connector.connect(
        user='root',
        password='Zinollini93',
        host='127.0.0.1',
        database='office'
    )
    cursor = connection.cursor()

    def get_offices_and_date(self, name, surname):
        query = '''
SELECT l.name, e.name, e.surname, el.date FROM location AS l, employees AS e, employees_location as el
WHERE l.id = el.location_id AND e.id = el.employee_id AND e.name = '{}' AND e.surname = '{}';
        '''.format(name, surname)

        self.cursor.execute(query)
        for (location, name, surname, date) in self.cursor:
            print(f"{location}, {name} {surname}, {date}")

    def get_employees_and_date(self, location):
        query = '''
SELECT e.name, e.surname, el.date FROM employees as e, location as l,  employees_location as el
WHERE el.location_id = l.id AND e.id = el.employee_id AND l.name = '{}';
        '''.format(location)

        self.cursor.execute(query)
        for (name, surname, date) in self.cursor:
            print(f"{name} {surname}, {date}")


    def get_employees_by_locatoin_and_date(self, location, date):
        query = '''
SELECT e.name, e.surname FROM employees as e, location as l, employees_location as el
WHERE el.location_id = l.id and l.name = '{}' and el.date = '{}' and el.employee_id = e.id;
        '''.format(location, date)

        self.cursor.execute(query)

        for (name, surname) in self.cursor:
            print(f"{name} {surname}")


    def get_inventory_by_employee(self, name, surname):
        query = '''
SELECT s.name FROM subject as s, employees as e WHERE s.employee_id = e.id and e.name = '{}' and e.surname = '{}' ;
        '''.format(name, surname)
        self.cursor.execute(query)
        for (name,) in self.cursor:
            print(f"{name}")


    def get_employee_by_subject(self, subject):
        query = '''
        SELECT e.name FROM employees as e, subject as s WHERE e.id = s.employee_id and s.name = '{}';
        '''.format(subject)
        self.cursor.execute(query)
        for (name,) in self.cursor:
            print(f"{name}")


    def get_common_subjects(self):
        query = '''
        SELECT name FROM subject WHERE employee_id IS NULL;
        '''
        self.cursor.execute(query)
        for (name,) in self.cursor:
            print(f"{name}")


    def get_subject_by_location(self, location):
        query = '''
        SELECT s.name FROM subject as s, location as l WHERE s.location_id = l.id and l.name = '{}';
        '''.format(location)
        self.cursor.execute(query)

        for (name,) in self.cursor:
            print(f"{name}")



    def get_salary_changes(self, name, surname):
        query = '''
        SELECT es.salary, es.date FROM employees_salary as es, employees as e
        WHERE es.employee_id = e.id and e.name = '{}' and e.surname = '{}';
        '''.format(name, surname)

        self.cursor.execute(query)

        for (salary, date) in self.cursor:
            print(f"{salary}, {date}")

    def set_salary(self):
        name = input("Enter employee's name\n")
        surname = input("Enter employee's surname\n")
        salary = float(input("Enter new salary\n"))
        new_date = str(date.today())
        query = '''
        SELECT id FROM employees WHERE name = '{}' AND surname = '{}' LIMIT 1;
        '''.format(name, surname)
        self.cursor.execute(query)
        employee_id = 0
        for (id,) in self.cursor:
            employee_id = id
        if employee_id:
            insert = '''
                    INSERT INTO employees_salary (employee_id, salary, date) VALUES ({}, {}, '{}')
                    '''.format(employee_id, salary, new_date)
            self.cursor.execute(insert)
            self.connection.commit()
        else:
            print("This employee doesn't exist")

    def set_new_employee(self):
        name = input("Enter new worker's name\n")
        surname = input("Enter new worker's surname\n")
        position = input("Enter worker's position\n")
        location = input("Enter employee's location\n")
        new_date = str(date.today())
        insert1 = '''
        INSERT INTO employees (name, surname, position) VALUES ('{}', '{}', '{}')
        '''.format(name, surname, position)
        self.cursor.execute(insert1)
        self.connection.commit()
        query1 = '''
        SELECT id FROM employees WHERE name = '{}' AND surname = '{}' LIMIT 1;
        '''.format(name, surname)
        employee_id = 0
        self.cursor.execute(query1)
        for (id,) in self.cursor:
            employee_id = id
        query2 = '''
        SELECT id FROM location WHERE name = '{}' LIMIT 1;
        '''.format(location)
        self.cursor.execute(query2)
        location_id = 0
        for (id,) in self.cursor:
            location_id = id

        insert2 = '''
        INSERT INTO employees_location (location_id, employee_id, date) VALUES ({}, {}, '{}')
        '''.format(location_id, employee_id, new_date)
        self.cursor.execute(insert2)
        self.connection.commit()

    def run(self):
        print('''
Choose the operation:
1 - Search in which locations and when certain employee worked
2 - Which employees and when worked in certain location
3 - What employees worked in the specified office for the specified period of dates
4 - What inventory does the specified employee use
5 - Which employee is the specified inventory item attached to?
6 - Which inventory items do not belong to any employee in the specified category
7 - What inventory items are in the specified location
8 - How has the employee's salary changed over time
9 - set new worker
10 - set salary
        ''')
        choice = input()
        if choice == '1':
            name = input("Enter employee's name\n")
            surname = input("Enter employee's surnmae\n")
            self.get_offices_and_date(name, surname)
            print("Do you want to continue?")
            answer = input()
            if answer == 'yes' or answer == 'Yes':
                self.run()
            else:
                sys.exit('Goodbye!')
        elif choice == '2':
            location = input("Enter location\n")
            self.get_employees_and_date(location)
            print("Do you want to continue?")
            answer = input()
            if answer == 'yes' or answer == 'Yes':
                self.run()
            else:
                sys.exit('Goodbye!')
        elif choice == '3':
            location = input("Enter location\n")
            date = input("Enter date in YYYY-MM-DD format\n")
            self.get_employees_by_locatoin_and_date(location, date)
            print("Do you want to continue?")
            answer = input()
            if answer == 'yes' or answer == 'Yes':
                self.run()
            else:
                sys.exit('Goodbye!')
        elif choice == '4':
            name = input("Enter employee's name\n")
            surname = input("Enter employee's surname\n")
            self.get_inventory_by_employee(name, surname)
            print("Do you want to continue?")
            answer = input()
            if answer == 'yes' or answer == 'Yes':
                self.run()
            else:
                sys.exit('Goodbye!')
        elif choice == '5':
            subject = input("Enter inventory's name\n")
            self.get_employee_by_subject(subject)
            print("Do you want to continue?")
            answer = input()
            if answer == 'yes' or answer == 'Yes':
                self.run()
            else:
                sys.exit('Goodbye!')
        elif choice == '6':
            self.get_common_subjects()
            print("Do you want to continue?")
            answer = input()
            if answer == 'yes' or answer == 'Yes':
                self.run()
            else:
                sys.exit('Goodbye!')
        elif choice == '7':
            location = input("Enter location's name\n")
            self.get_subject_by_location(location)
            print("Do you want to continue?")
            answer = input()
            if answer == 'yes' or answer == 'Yes':
                self.run()
            else:
                sys.exit('Goodbye!')
        elif choice == '8':
            name = input("Enter employee's name\n")
            surname = input("Enter employee's surname\n")
            self.get_salary_changes(name, surname)
            print("Do you want to continue?")
            answer = input()
            if answer == 'yes' or answer == 'Yes':
                self.run()
            else:
                sys.exit('Goodbye!')
        elif choice == '9':
            self.set_new_employee()
            print("Do you want to continue?")
            answer = input()
            if answer == 'yes' or answer == 'Yes':
                self.run()
            else:
                sys.exit('Goodbye!')
        elif choice == '10':
            self.set_salary()
            print("Do you want to continue?")
            answer = input()
            if answer == 'yes' or answer == 'Yes':
                self.run()
            else:
                sys.exit('Goodbye!')
        else:
            print("There's no such command")
            self.run()


admin = Admin()
admin.run()
