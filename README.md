# Intern Id: CITS2067
# Natural_Language_generator
This project is a simple Natural Language Generator (NLG) developed using Python. It generates text based on patterns learned from training data using a basic Markov Chain approach. The application predicts the next word and creates meaningful sentences automatically.A Markov Chain is a mathematical model that predicts the next state or word based only on the current state or word. In this NLG project, the next word is chosen using the current word without considering earlier words. 
This helps generate sentences that follow the patterns learned from the training data.Features like beginner-friendly Python project uses Random Module and Markov Chain Algorithm Used Python requests library for Natural Language Generation Structure nlg-project/ │ ├── nlg.py ├── README.md └── requirements.txt Installation

# Sample code:

import random


text = """
Ravi likes to play cricket with his friends after school.
Priya enjoys reading books in the library every evening.
The weather was pleasant and everyone went for a walk.
A little boy found a lost puppy near the market.
The family planned a picnic by the river on Sunday.
Students worked together to complete their science project.
"""


words = text.split()

model = {}

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]

    if current_word not in model:
        model[current_word] = []

    model[current_word].append(next_word)


def generate_text():

    # Possible starting words
    start_words = ["Ravi", "Priya", "The", "A", "Students"]

    current_word = random.choice(start_words)
    sentence = [current_word]

    # Continue until a full stop is found
    while not current_word.endswith("."):

        if current_word in model:
            current_word = random.choice(model[current_word])
            sentence.append(current_word)
        else:
            break

    return " ".join(sentence)

print("=== Natural Language Generator ===")

n = int(input("Enter number of texts to generate: "))

for i in range(n):
    print(f"\nGenerated Text {i + 1}:")
    print(generate_text())

print("\n=== Generation Complete ===")


