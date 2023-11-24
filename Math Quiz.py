import random
import time

O = ["+", "-", "*"]
MIN =  int(input('Enter minimum value: '))
MAX =  int(input('Enter maximum value: '))
TOTAL = int(input('Enter number of problems: '))


def problem():
    a = random.randint(MIN, MAX)
    b = random.randint(MIN, MAX)
    c = random.choice(O)

    expr = str(a) + " " + c + " " + str(b)
    answer = eval(expr)
    return expr, answer


correct = 0
input("Press enter to start!")
print("----------------------")

t1 = time.time()

for i in range(TOTAL):
    expr, answer = problem()
    while True:
        d = input("Problem -" + str(i + 1) + ": " + expr + " = ")
        if d == str(answer):
            correct += 1
            break
        continue

t2 = time.time()
total_time = round(t2 - t1, 2)

print("----------------------")
print("You finished in", total_time, "seconds!")
print("accuracy=", (correct / TOTAL) * 100)
