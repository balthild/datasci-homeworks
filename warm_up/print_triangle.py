num = int(input("Lines: "))
width = 2 * num - 1

for i in range(num):
    star_num = (2 * i + 1)
    space_num = int((width - star_num) / 2)

    stars = '*' * star_num
    spaces = ' ' * space_num

    print(spaces + stars + spaces)
