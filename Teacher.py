class teacher():
    def __init__(self,nam,reg):
        self.name =nam
        self.register_num = reg
    def display(self):
        print("Name:",self.name)
        print("Register_Number",self.register_num)

t1 = teacher("Mythili",1)
t2 = teacher("Manoj",2)
t1.display()
t2.display()
