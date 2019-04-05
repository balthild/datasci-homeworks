from random import randint

n = int(input("Please input number of questions: "))
score = 0

for i in range(n):
    a = randint(0, 9)
    b = randint(0, 9)

    ans = int(input(f"{a} + {b} = "))
    if ans == a + b:
        score += 10

print(f"Total score: {n*10}. Your score: {score}.")
