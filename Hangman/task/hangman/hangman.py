# Write your code here
import random
print("""
H A N G M A N
""")
word = ["python", "java", "kotlin", "javascript"]
guess = input("Guess the word: ")
secret = random.choice(word)

print("You survived!" if guess == secret else "You are hanged!")
