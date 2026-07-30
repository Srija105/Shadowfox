import random

# List of words
words = ["python", "computer", "program", "hangman", "developer"]

# Select a random word
word = random.choice(words)

# Game setup
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("===== HANGMAN GAME =====")

while wrong_guesses < max_attempts:
    # Display the word
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong Attempts Left:", max_attempts - wrong_guesses)

    # Check win condition
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")

# Loss condition
if wrong_guesses == max_attempts:
    print("\n💀 Game Over!")
    print("The correct word was:", word)

# Play again option
choice = input("\nDo you want to play again? (yes/no): ").lower()

if choice == "yes":
    print("Run the program again to play!")
else:
    print("Thank you for playing!")