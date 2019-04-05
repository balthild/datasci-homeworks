from random import randint

rand50 = [str(randint(1, 100)) for i in range(50)]

with open('1.csv', 'w+') as f:
    f.write(', '.join(rand50))
    f.write('\n')

with open('1.csv', 'r') as f:
    sl: str = f.readline()

rand50_rev = [x.strip() for x in sl.split(',')]
rand50_rev.reverse()

with open('1.csv', 'a') as f:
    f.write(', '.join(rand50_rev))
    f.write('\n')
