class employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
class manager(employee):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.department = dept
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.department)
m1 = manager("Mythili",9000,"IT")
m1.display()
