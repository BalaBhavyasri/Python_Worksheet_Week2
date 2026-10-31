class Employee:
    def __init__(self, employee_id, employee_name, salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.salary = salary

    def display_details(self):
        print("Employee ID:", self.employee_id)
        print("Employee Name:", self.employee_name)
        print("Salary:", self.salary)
        print()

e1 = Employee(101, "Anil", 30000)
e2 = Employee(102, "Bhavya", 40000)
e3 = Employee(103, "Rahul", 35000)

e1.display_details()
e2.display_details()
e3.display_details()