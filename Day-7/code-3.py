#Parent Class
class Animal:
    
    def speak(self):
        print("Animal is making a sound")

#child Class
class Dog (Animal):
    def speak(self):
        print("Dog is barking   !!!!!!")


#creating an object of the child class
my_dog = Dog()
my_dog.speak()