class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
    def displaycar(self):
        print "This is a", str(self.color), str(self.model), "with", str(self.mpg), "MPG."
    def drivecar(self):
        self.condition = "used"
        print self.condition

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.battery_type = battery_type
        self.model = model
        self.color = color
        self.mpg = mpg
    def drive_car(self):               
        condition = "like new"
        self.condition = condition
        print condition
my_car = ElectricCar("cbr", "silver", 32, "molten salt")
print my_car.condition
my_car.drive_car() 

print my_car.condition
