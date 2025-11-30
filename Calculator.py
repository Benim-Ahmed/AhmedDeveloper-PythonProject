num1 = float(input("Please enter first number: "))
num2 = float(input("Pleasae enter second number: "))

print(f"Sum of {num1} and {num2} = ", num1 + num2)
print(f"Difference of {num1} and {num2} = ", num1 - num2)
print(f"Product of {num1} and {num2} = ", num1 * num2)
if num2 != 0:
    print(f"Quotient of {num1} and {num2} = ", num1 / num2)
elif num2 == 0:
    print("Cannot divide by zero! enter a valid number")