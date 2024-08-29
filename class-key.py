class Person:
    def __init__(self):
        self.dudes = {}

    def add(self, name, age, country):
        self.dudes[name] = {"age": age, "country": country}
        
    def view(self):
        print(self.dudes)
        for name, details in self.dudes.items():
            print(f"Name: {name}, Age: {details["age"]}, Country: {details["country"]}")
        

p1 = Person()


p1.add("hej", 33, "france")
p1.add("då", 233, "englis")
p1.view()