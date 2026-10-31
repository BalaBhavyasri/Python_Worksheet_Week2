students = ["Anil", "Bhavya", "Rahul", "Sneha", "Ravi"]

with open("students.txt", "w") as file:
    for name in students:
        file.write(name + "\n")

with open("students.txt", "r") as file:
    names = file.readlines()

print("Student Names:")

for name in names:
    print(name.strip())

print("Total Students:", len(names))