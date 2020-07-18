# Write your code here
import random

print("""
H A N G M A N
""")
word = ["python", "java", "kotlin", "javascript"]
secret = random.choice(word)

guess = '-' * len(secret)
guessed = []

for _ in range(0, 8):
    print(guess)
    letter = input("Input a letter: ")
    if letter in secret and letter not in guessed:
        occurrence = [i for i in range(len(secret)) if secret[i] == letter]
        for index in occurrence:
            guess = guess[:index] + letter + guess[index + 1:]
        guessed.append(letter)
    else:
        print("No such letter in the word")
    print()


print("""
Thanks for playing!
We'll see how well you did in the next stage
""")

# print("You survived!" if guess == secret else "You are hanged!")
