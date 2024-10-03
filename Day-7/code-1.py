#Defining a class
class Car:
    
    def __init__(self,color,model):
        self.color = color
        self.model = model
    
    def start(self):
        print(f"The {self.color} {self.model} is staring.")


#creating a Object
my_car = Car("Red","Honda Civic")
my_car.start()

















#car is an class
#my_car is an Object