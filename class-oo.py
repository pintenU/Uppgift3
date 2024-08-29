import os

class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
    
    def show(self):
        return f"{self.make} {self.model} ({self.color})"
    
    
def display_cars():
    os.system('cls')
    print("\nLIST OF CARS")
    for index, car in enumerate(cars, 1):
        print(f"{index}) {car.show()}")


os.system("cls")
# List to store all car instances
cars = []

while True:
    print("""
\nADD A CAR
Enter nothing to exit - delete by choosing the corresponding number.
""")
    make = input("Enter a make: ")
    if make.isnumeric():
        try:
            cars.pop(int(make-1))
            os.system("cls")
            continue
        except:
            print("Car does not exist")
        
    model = input("Enter a model: ")
    color = input("Enter car color (Type nothing to quit): ")
    
        
    if color == "":
        break
    
    # Create a new Car instance and add it to the list
    cars.append(Car(make, model, color))

    # View all cars added
    display_cars()
