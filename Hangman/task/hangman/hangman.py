# Write your code here
import random

print("""H A N G M A N""")
word = ["python", "java", "kotlin", "javascript"]
secret = random.choice(word)

guess = '-' * len(secret)
guessed = []

attempt = 8

while attempt > 0:
    print("\n" + guess)
    letter = input("Input a letter: ")
    if letter in guessed:
        print("No improvements")
        attempt -= 1
    elif letter in secret:
        occurrence = [i for i in range(len(secret)) if secret[i] == letter]
        for index in occurrence:
            guess = guess[:index] + letter + guess[index + 1:]
        guessed.append(letter)
        if guess == secret:
            break
    else:
        print("No such letter in the word")
        attempt -= 1

if attempt == 0:
    print("You are hanged!")
else:
    print("""You guessed the word!
You survived!
    """)
