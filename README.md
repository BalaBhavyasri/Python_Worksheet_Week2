# Python Full Stack – Week 2 Worksheet
This repository contains solutions to the **Python Full Stack Development – Week 2 Worksheet**.

The worksheet focuses on Object-Oriented Programming (OOP), exception handling, dictionaries, file handling, lambda functions, list comprehension, and real-world Python mini projects.

## Technologies Used

- **Language:** Python 3
- **IDE:** Visual Studio Code
- **Concepts:** OOP, Inheritance, Polymorphism, Exception Handling, File Handling
- **Libraries:** Python Standard Library

## Questions and Programs

### Q1. Class and Object Creation

**Aim:** Create a Student class using Python.

**Description:**
- Create a class named `Student`.
- Define attributes: `name`, `roll_number`, and `marks`.
- Create a method `display_details()`.
- Create two student objects and display their details.

**Concepts:** Classes, Objects, Methods.

### Q2. Constructor and Instance Variables

**Aim:** Demonstrate constructors and instance variables.

**Description:**
- Create an `Employee` class.
- Use the `__init__()` constructor.
- Initialize employee ID, employee name, and salary.
- Create three employee objects.
- Display employee details.

**Concepts:** Constructors, Instance Variables, Object Creation.

### Q3. Inheritance

**Aim:** Implement inheritance using Vehicle and Car classes.

**Description:**
- Create a parent class `Vehicle`.
- Define `start()` and `stop()` methods.
- Create a child class `Car`.
- Add a `drive()` method.
- Demonstrate inheritance by calling all methods.

**Concepts:** Inheritance, Parent Class, Child Class.

### Q4. Method Overriding

**Aim:** Demonstrate method overriding in Python.

**Description:**
- Create a parent class `Animal`.
- Define a `sound()` method.
- Create subclasses `Dog` and `Cat`.
- Override the `sound()` method in both subclasses.

**Concepts:** Method Overriding, Inheritance.

### Q5. Polymorphism

**Aim:** Calculate the areas of different shapes using polymorphism.

**Description:**
- Create `Circle` and `Rectangle` classes.
- Implement an `area()` method in each class.
- Accept dimensions from the user.
- Calculate and display the areas.

**Concepts:** Polymorphism, Methods, Mathematical Operations.

### Q6. Exception Handling

**Aim:** Handle errors during division operations.

**Description:**
- Accept two numbers from the user.
- Perform division.
- Handle `ZeroDivisionError`.
- Handle `ValueError`.
- Display appropriate error messages.

**Concepts:** Try-Except, Exception Handling.

### Q7. Dictionary-Based Student Management System

**Aim:** Manage student information using dictionaries.

**Description:**
- Store student names, marks, and grades.
- Add five students.
- Display all student details.
- Find the student with the highest marks.

**Concepts:** Dictionaries, Loops, Conditional Statements.

### Q8. File Handling

**Aim:** Store and retrieve student names using file operations.

**Description:**
- Create a file named `students.txt`.
- Store five student names.
- Read and display all names.
- Count the total number of students.

**Concepts:** File Handling, `open()`, `write()`, `read()`.

### Q9. Lambda and List Comprehension

**Aim:** Perform list operations using lambda functions and list comprehension.

**Description:**
- Create a list containing numbers from 1 to 10.
- Generate squares using list comprehension.
- Extract even numbers using a lambda function.

**Expected Output:**

```text
Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Even Numbers: [2, 4, 6, 8, 10]
```

**Concepts:** Lambda Functions, List Comprehension, Filtering.

### Q10. Bank Account Management System

**Aim:** Develop a menu-driven bank account application.

**Description:**
- Create a `BankAccount` class.
- Store account number, account holder name, and balance.
- Implement `deposit()`, `withdraw()`, and `check_balance()` methods.
- Prevent withdrawals exceeding the available balance.
- Display appropriate messages.

**Menu:**

```text
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
```

**Concepts:** OOP, Encapsulation, Conditional Statements, Menu-Driven Programming.

### Q11. Library Management System

**Aim:** Develop a library management system using Object-Oriented Programming.

**Description:**
- Create a library management class.
- Implement functionality to add books.
- Allow users to issue books.
- Allow users to return books.
- Display available books.
- Manage book information using lists and dictionaries.

**Concepts:** Classes, Objects, Lists, Dictionaries, Methods.

## Project Structure

```text
Python-FullStack-Week2/
│
├── Q1.py
├── Q2.py
├── Q3.py
├── Q4.py
├── Q5.py
├── Q6.py
├── Q7.py
├── Q8.py
├── Q9.py
├── Q10.py
├── Q11.py
│
├── README.md
└── students.txt
```

*Note: This is a suggested folder structure. The `students.txt` file is created by the Q8 program.*

## How to Run the Programs

**Step 1:** Install Python 3.

**Step 2:** Open Visual Studio Code.

**Step 3:** Clone or download the repository.

**Step 4:** Open the project folder in VS Code.

**Step 5:** Open the terminal.

**Step 6:** Run any Python program.

Example:

```bash
python Q1.py
```

To run the Bank Account Management System:

```bash
python Q10.py
```

To run the Library Management System:

```bash
python Q11.py
```

## Learning Outcomes

After completing this worksheet, students will be able to:

1. Create classes and objects in Python.
2. Implement constructors and instance variables.
3. Understand inheritance and method overriding.
4. Apply polymorphism to solve problems.
5. Handle runtime exceptions.
6. Manage information using dictionaries.
7. Perform file reading and writing operations.
8. Use lambda functions and list comprehension.
9. Develop menu-driven Python applications.
10. Build basic real-world applications using OOP.

## Conclusion

This worksheet provides practical experience with important Python programming concepts. The exercises strengthen problem-solving skills and demonstrate how Python can be used to develop real-world applications such as Bank Account Management and Library Management Systems.

