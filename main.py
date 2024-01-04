import random
import time
import os
import json
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

O = ["+", "-", "*"]
MIN = int(input("Enter minimum value: "))
MAX = int(input("Enter maximum value: "))
TOTAL = int(input("Enter number of problems: "))


def problem():
    # a = random.randint(MIN, MAX)
    # b = random.randint(MIN, MAX)
    # c = random.choice(O)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Generate 1 maths question using numbers between {MIN} and {MAX}. Give the output in a json where one field is the question called 'question' and the other is the answer called 'answer'.",
            }
        ],
        model="gpt-3.5-turbo",
    )

    result = json.loads(chat_completion.choices[0].message.content)

    print(result["question"], result["answer"])

    return result

    # expr = str(a) + " " + c + " " + str(b)
    # answer = eval(expr)
    # return expr, answer


correct = 0
input("Press enter to start!")
print("----------------------")

t1 = time.time()

for i in range(TOTAL):
    problem()
    # expr, answer = problem()
    # while True:
    #     d = input("Problem -" + str(i + 1) + ": " + expr + " = ")
    #     if d == str(answer):
    #         correct += 1
    #         break
    #     continue

t2 = time.time()
total_time = round(t2 - t1, 2)

print("----------------------")
print("You finished in", total_time, "seconds!")
print("accuracy=", (correct / TOTAL) * 100)
