import random
words = ["apple", "banana", "orange", "mango", "grapes"]
word = random.choice(words)

guessed_letters = []
tries = 6

while tries > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct!")
    else:
        guessed_letters.append(guess)
        tries -= 1
        print("Wrong! Tries left:", tries)

if tries == 0:
    print("Game Over! The word was:", word)