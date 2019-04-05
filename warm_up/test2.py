import random

# Generate two random integers within 0 and 10
a = int(random.random() * 10)
b = int(random.random() * 10)

# Prompt the user to ask for answer
c = int(input(f"{a} + {b} = "))

# Determine whether the answer is correct
if a + b == c:
    print('Correct!')
else:
    print(f'Wrong. The answer is {a+b}.')
