# Taking numbers from user
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

# Calculations
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

# Division (handle divide by zero)
if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Cannot divide by zero")