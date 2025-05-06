class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    def beAnnoying(self):
        print("annoying")
cat1=Cat()
cat1.beAnnoying()