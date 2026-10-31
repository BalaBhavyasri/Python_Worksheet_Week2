try:
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input. Enter numbers only.")