# Write your code here
import random

print("""H A N G M A N""")

play = False
while True:
    print("Type \"play\" to play the game, \"exit\" to quit:")
    if input() == "play":
        play = True
        break
    if input() == 'exit':
        break

if play:
    word = ["python", "java", "kotlin", "javascript"]
    secret = random.choice(word)

    guess = '-' * len(secret)
    guessed = []

    attempt = 8

    while attempt > 0:
        print("\n" + guess)
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")
            guessed.append(letter)
        elif not letter.islower():
            print("It is not an ASCII lowercase letter")
            guessed.append(letter)
        elif letter in guessed:
            print("You already typed this letter")
        elif letter in secret:
            occurrence = [i for i in range(len(secret)) if secret[i] == letter]
            for index in occurrence:
                guess = guess[:index] + letter + guess[index + 1:]
            guessed.append(letter)
            if guess == secret:
                break
        else:
            print("No such letter in the word")
            guessed.append(letter)
            attempt -= 1

    if attempt == 0:
        print("You are hanged!")
    else:
        print("""You guessed the word!
    You survived!
        """)
