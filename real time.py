class laptop:
    def __init__(self):
        self.name = ""
        self.price = int()
        self.processor = ""
        self.RAM = ""
    def display(self):
        print("Price:",self.price)
        print("Processor:",self.processor)
        print("RAM:",self.RAM)
HP = laptop()
DELL = laptop()
LENOVA = laptop()
HP.name="HP"
DELL.name="DELL"
LENOVA.name="LENOVA"
HP.price = 75000
DELL.price = 90000
LENOVA.price = 80000
DELL.processor= "i5"
HP.processor = "i5"
LENOVA.processor = "i7"
HP.RAM = "8GB"
DELL.RAM = "16GB"
LENOVA.RAM = "32GB"
print(HP.name)
HP.display()
print(DELL.name)
DELL.display()
print(LENOVA.name)
LENOVA.display()
