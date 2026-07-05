import random

def play_hangman():
    # 1. Setup
    word_list = ["python", "coding", "computer", "challenge", "developer"]
    secret_word = random.choice(word_list)
    guessed_letters = []
    incorrect_guesses = 0
    max_guesses = 6

    print("Welcome to Hangman!")

    # 2. Game Loop
    while incorrect_guesses < max_guesses:
        # Display current word status
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print(f"\nWord: {display_word}")
        print(f"Incorrect guesses left: {max_guesses - incorrect_guesses}")
        
        # Check for win condition
        if "_" not in display_word:
            print("Congratulations! You guessed the word:", secret_word)
            break

        # Get user input
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in secret_word:
            print("Good job!")
            guessed_letters.append(guess)
        else:
            print("Wrong!")
            guessed_letters.append(guess)
            incorrect_guesses += 1

    # 3. Game Over
    if incorrect_guesses == max_guesses:
        print(f"\nGame Over! The word was: {secret_word}")

# Run the game
if __name__ == "__main__":
    play_hangman()