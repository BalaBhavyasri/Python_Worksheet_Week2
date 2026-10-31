students = {
    "Anil": {"marks": 85, "grade": "A"},
    "Bhavya": {"marks": 95, "grade": "A+"},
    "Rahul": {"marks": 78, "grade": "B"},
    "Sneha": {"marks": 90, "grade": "A+"},
    "Ravi": {"marks": 70, "grade": "B"}
}

print("Student Details:")

for name, details in students.items():
    print("Name:", name)
    print("Marks:", details["marks"])
    print("Grade:", details["grade"])
    print()

topper = max(students, key=lambda x: students[x]["marks"])

print("Student with Highest Marks:")
print("Name:", topper)
print("Marks:", students[topper]["marks"])