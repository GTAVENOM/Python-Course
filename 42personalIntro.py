class Person:
    def __init__(self, name):
        self.name=name

    def talk(self):
        print(f'Hello I\'m {self.name}')


person1=Person("John")
person1.talk()