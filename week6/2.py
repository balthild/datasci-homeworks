import csv

data = [
    ('name1', 22, 82),
    ('name2', 23, 88),
    ('name3', 19, 97),
    ('name4', 18, 73),
    ('name5', 24, 98),
    ('name6', 22, 94),
]

data.sort(key=lambda r: r[2], reverse=True)

data = [(i + 1,) + r for i, r in enumerate(data)]

with open('2.csv', 'w+') as f:
    writer = csv.writer(f)

    writer.writerow(('No.', 'Name', 'Age', 'Score'))
    writer.writerows(data)
