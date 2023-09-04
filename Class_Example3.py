class vehicle():
    def start(self):
        print("Vehicle started")
class car(vehicle):
    def start(self):
        print("car started")
c1 = car()
c1.start()
