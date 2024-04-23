# Header-----------------------------------------------------
#Name Amanda Hinnerichs
#Date 4/15/2024
#Program EX14-1
#Description: Simple text base calculator


# Functions --------------------------------------------------
class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

# Main----------------------------------------------------------------
print('14.1 Simple Calculator')
n1 = int(input(f'\nPlease choose the first number: '))
n2 = int(input('Please choose another number: '))
calc = Calculator(n1,n2)
result = calc.add()
print(f' \n{n1} + {n2} = {result}')
result = calc.subtract()
print(f' \n{n1} - {n2} = {result}')
result = calc.multiply()
print(f' \n{n1} * {n2} = {result}')
result = calc.divide()
print(f' \n{n1} / {n2} = {result}')









calc = Calculator(4,4)
result = calc.add