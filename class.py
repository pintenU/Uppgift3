import os

class Car:    #en klass har alltid stor bokstav
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def view_car(self):
        return f"{self.make} - {self.model} ({self.color})"
    

os.system("cls")

cars = []

cars.append(Car("Lada", "Kalina", "Yellow"))

for car in cars:
    print(car.view_car())

#Gör ett program som man kan mata in bilar själv


