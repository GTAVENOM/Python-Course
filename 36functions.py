def hello():
    print('Hello World!')


def hiUser(firstName, lastName):
    print(f'Hi {firstName} {lastName}!')
print('Start')
hello()
hiUser("John", "Smith")
hiUser(lastName="Smith", firstName="John")
print('End')