import time
import os
import json

import questionary
from openai import OpenAI
from colorama import init
from termcolor import colored

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

init()


num_of_questions = questionary.text(
    "How many questions do you want to generate?",
    validate=lambda val: int(val) > 0,
).ask()

difficulty = questionary.select(
    "What difficulty do you want?",
    choices=[
        "Easy",
        "Medium",
        "Hard",
    ],
).ask()

operations = questionary.checkbox(
    "What operations do you want?",
    choices=[
        "+",
        "-",
        "*",
        "/",
        "^",
        "sqrt",
    ],
).ask()


print()
print("----------------------")
print()


def problem():
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Generate 1 maths question using numbers between 1 and 100. Difficulty level is {difficulty} (easy - middle school level, medium - high school level, hard - high school level but harder). The operations the questions can include are: {','.join(operations)} Give the output in a json where one field is the question called 'question' and the other is the answer called 'answer'.",
            }
        ],
        model="gpt-3.5-turbo",
    )

    result = json.loads(chat_completion.choices[0].message.content)

    return result


start = time.time()
correct = 0

for i in range(int(num_of_questions)):
    result = problem()
    print("Question:", colored(result["question"], "blue"))
    answer = input("Answer: ")
    if answer == result["answer"]:
        print(colored("Correct!", "green"))
        correct += 1
    else:
        print(colored("Incorrect!", "red"))
        print("The answer is", result["answer"])

    print()

end = time.time()

print("----------------------")
print()

print("You finished in", colored(round(end - start, 2), "green"), "seconds!")
print(
    "Your accuracy is",
    colored(round((correct / int(num_of_questions)) * 100, 2), "blue"),
)
