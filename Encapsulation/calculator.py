# Write a Python program to create a calculator class.
# The class should have four private variables: num1, num2, result, and operation.
# The class should also have a constructor that takes two numbers as arguments,
# a getter method for the result, and a method for performing the operation.

class  Calculator:
    def __init__(self,num1, num2):
        self.__num1=num1
        self.__num2=num2
        self.__result = None
        self.__operation = None

    def get_result(self):
        return self.__result

    def perform_operation(self, operation):
        if operation == '+':
            self.__result = self.__num1 + self.__num2
        elif operation == '-':
            self.__result = self.__num1 - self.__num2
        elif operation == '*':
            self.__result = self.__num1 * self.__num2
        elif operation == '/':
            if self.__num2 != 0:
                self.__result = self.__num1 / self.__num2
            else:
                print("Cannot divide by zero.")
                return
        else:
            print("Invalid operation.")
            return

        self.__operation = operation
        print(f"Performed  operation : {self.__operation}")


c1 = Calculator(15, 31)
c1.perform_operation('+')
print(f"Result:  {c1.get_result() }")