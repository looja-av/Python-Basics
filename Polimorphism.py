class Vehicle():
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year

    def move(self):
        print("Road travel")

class Car(Vehicle):
    pass

class Plane(Vehicle):
    def move(self):
        print("fly")

car1=Car("Toyota",34)
Plane1=Plane("Emirates",23)

for x in (car1,Plane1):
    print(x.brand)
    print(x.year)
    x.move()
