class calculator():
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b
    def addition(self):
        print("Sum is: ",self.num1 + self.num2)
    def subtraction(self):
        print("Subtraction is: ", self.num1 - self.num2)
    def multiplication(self):
        print("Multiplication is: ",self.num1 * self.num2)
    def division(self):
        print("Division is: ", self.num1 / self.num2)
value = calculator(5,2)
value.addition()
value.subtraction()
value.multiplication()
value.division()
