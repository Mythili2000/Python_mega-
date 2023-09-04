class rectangle():
    def __init__(self,w,h):
        self.width = w
        self.height = h
    def area_rectange(self):
        return self.width * self.height
    def perimeter_rectangle(self):
        return 2*(self.width+self.height)

    def display(self):
        print("Area of rectangle:",self.area_rectange())
        print("Perimeter of rectangle:",self.perimeter_rectangle())
r1 = rectangle(15,5)
r1.display()