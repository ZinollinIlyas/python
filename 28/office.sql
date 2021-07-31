CREATE DATABASE IF NOT EXISTS office;

USE office;

CREATE TABLE IF NOT EXISTS location (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS employees(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(55) NOT NULL,
    surname VARCHAR(55) NOT NULL,
    position VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS category(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS subject(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    category_id INT NOT NULL,
    location_id INT NOT NULL,
    employee_id INT NULL,
    registration_date DATE NOT NULL,
    FOREIGN KEY (category_id) REFERENCES category (id),
    FOREIGN KEY (location_id) REFERENCES location (id),
    FOREIGN KEY (employee_id) REFERENCES employees (id)
);

CREATE TABLE IF NOT EXISTS employees_location(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    location_id INT NOT NULL,
    employee_id INT NULL,
    date DATE NOT NULL,
    FOREIGN KEY (location_id) REFERENCES location (id),
    FOREIGN KEY (employee_id) REFERENCES employees (id)
);

CREATE TABLE IF NOT EXISTS employees_salary(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    employee_id INT NOT NULL,
    salary FLOAT NOT NULL,
    date DATE NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees (id)
);



INSERT INTO location (name) VALUES ('office'),
                                   ('dining room'),
                                   ('rest room');

INSERT INTO employees (name, surname, position) VALUES ('John', 'Doe', 'manager'),
                                                       ('Bob', 'Richards', 'accountant'),
                                                       ('James', 'May', 'web-developer');

INSERT INTO employees_location (location_id, employee_id, date) VALUES (1, 1, '2018-02-15'),
                                                                       (1, 2, '2019-10-23'),
                                                                       (1, 3, '2020-03-14');

INSERT INTO employees_salary (employee_id, salary, date) VALUES (1, 1000, '2018-02-15'),
                                                                (2, 1000, '2019-10-23'),
                                                                (3, 3000, '2020-03-14'),
                                                                (1, 1500, '2020-02-15');

INSERT INTO category (name) VALUES ('furniture'),
                                   ('computer equipment'),
                                   ('consumer electronics');

INSERT INTO subject (name, description, category_id, location_id, employee_id, registration_date)
VALUES ('table', 'working environment', 1, 1, 2, '2019-08-10'),
       ('coffee-machine', 'makes delicious coffee', 3, 2, null, '2018-05-05'),
       ('computer', 'working tool', 2, 1, 3, '2019-07-15');



SELECT l.name, e.name, e.surname, el.date FROM location AS l, employees AS e, employees_location as el
WHERE l.id = el.location_id AND e.id = el.employee_id AND e.name = 'John';

SELECT e.name, e.surname, el.date FROM employees as e, location as l,  employees_location as el
WHERE el.location_id = l.id AND e.id = el.employee_id AND l.name = 'office';

SELECT e.name, e.surname FROM employees as e, location as l, employees_location as el
WHERE el.location_id = l.id and l.name = 'office' and el.date = '2018-02-15' and el.employee_id = e.id;

SELECT s.name FROM subject as s, employees as e WHERE s.employee_id = e.id and e.name = 'James' ;

SELECT e.name FROM employees as e, subject as s WHERE e.id = s.employee_id and s.name = 'table';

SELECT name FROM subject WHERE employee_id IS NULL;

SELECT s.name FROM subject as s, location as l WHERE s.location_id = l.id and l.name = 'office';

SELECT es.salary, es.date FROM employees_salary as es, employees as e
WHERE es.employee_id = e.id and e.name = 'John';




