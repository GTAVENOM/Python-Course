command=input('type "help" for all commands: ').lower()
state=0
while True:
    if command=='quit' and state==0:
        break
    elif command=='quit' and state==1:
        print('The car is on. Turn it off to exit the car.')
        break
    if command=='start':
        if state==0:
            print('The car has started. Vroom Vroom')
            state=1
        else:
            print('The car has already been turned on.')

    elif command=='stop':
        if state==1:
            print('The car has stopped.')
            state=0
        else:
            print('The car has already been stopped.')

    elif command=='help':
        print('''start- to start the car
        stop- to stop the car
        quit- to exit the car''')

    else:
        print('I don\'t understand that.')
    command=input('Enter your command: ').lower()#dont repeat yourself(dry). lower casing the command
print('Exiting the car.')