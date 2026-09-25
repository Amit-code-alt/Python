def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("=== Simple Calculator ===")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Choose an operation (1-4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    print("Answer:", add(num1, num2))

elif choice == "2":
    print("Answer:", subtract(num1, num2))

elif choice == "3":
    print("Answer:", multiply(num1, num2))

elif choice == "4":
    print("Answer:", divide(num1, num2))

else:
    print("Invalid choice")
