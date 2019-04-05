cl = int(input("Please input class number: "))

classes = {
    1: '8:30 - 10:05',
    2: '10:25 - 12:00',
    3: '13:55 - 15:30',
    4: '15:50 - 17:25',
}

print(classes.get(cl, 'Invalid input (1-4).'))
