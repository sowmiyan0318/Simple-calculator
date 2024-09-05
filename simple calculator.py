class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed"

# Create an instance of the Calculator class
my_calculator = Calculator()

# Perform calculations
print(my_calculator.add(5, 3))  # Output: 8
print(my_calculator.subtract(10, 4))  # Output: 6
print(my_calculator.multiply(7, 2))  # Output: 14
print(my_calculator.divide(12, 3))  # Output: 4.0
print(my_calculator.divide(10, 0))  # Output: Error: Division by zero is not allowed
