# Write your code here
import random

def masked_word(word: str) -> str:
    return word[0:3] + '-' * (len(word) - 3)

print("""
H A N G M A N
""")
word = ["python", "java", "kotlin", "javascript"]
secret = random.choice(word)
guess = input("Guess the word " + masked_word(secret) + ": ")

print("You survived!" if guess == secret else "You are hanged!")
