class shape():
    def area(self):
        return 0
class rectangle(shape):
    def area(self,a,b):
        return a * b
r1 = rectangle()
print(r1.area(5,3))
