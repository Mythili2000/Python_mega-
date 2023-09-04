class student:
    def __init__(self):
        self.name="Mythili"
        self.register_number = 0
    def display(self):
        print("Name:",self.name)
        print("Register_Number:",self.register_number)
s1 = student()
s2 = student()
s1.name="manoj"
s1.register_number=1

s2.name="karthick"
s2.register_number=2

s1.display()
s2.display()
