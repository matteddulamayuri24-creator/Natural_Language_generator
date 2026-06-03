import random

# Training data
text = """
Ravi likes to play cricket with his friends after school.
Priya enjoys reading books in the library every evening.
The weather was pleasant and everyone went for a walk.
A little boy found a lost puppy near the market.
The family planned a picnic by the river on Sunday.
Students worked together to complete their science project.
"""


# Convert text into words
words = text.split()

# Build Markov model
model = {}

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]

    if current_word not in model:
        model[current_word] = []

    model[current_word].append(next_word)

# Generate text
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

# Main program
print("=== Natural Language Generator ===")

n = int(input("Enter number of texts to generate: "))

for i in range(n):
    print(f"\nGenerated Text {i + 1}:")
    print(generate_text())

print("\n=== Generation Complete ===")
