class car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def display(self):
        print("Make:",self.make)
        print("Model:",self.model)
        print("Year:",self.year)

honda = car("classic","Ivtech",1999)
honda.display()

