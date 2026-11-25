
class Animal:
    def eat(self):
        print("Animals can eat")


class Dog(Animal):
    def bark(self):
        print("Dog can bark")


d = Dog()

d.eat()
d.bark()