import random

# List of predefined words
words = ["apple", "tiger", "house", "python", "banana"]

# Randomly choose a word
word = random.choice(words)

# Create blanks for the hidden word
display = ["_"] * len(word)

# Variables
wrong_guesses = 0
max_wrong = 6
guessed_letters = []

print("Welcome to Hangman!")

# Game loop
while wrong_guesses < max_wrong and "_" in display:
    print("\nWord:", " ".join(display))
    print("Guessed letters:", guessed_letters)
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
    else:
        guessed_letters.append(guess)

        if guess in word:
            # Reveal the letter(s)
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
            print("Correct!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

# End of game
if "_" not in display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The correct word was:", word)