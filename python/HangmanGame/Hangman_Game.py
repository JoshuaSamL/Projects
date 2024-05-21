import random as rand

# Dictionary with categories as keys and word lists as values
word_categories = {
    "colors": ["azure", "scarlet", "crimson", "magenta"],
    "musical instruments": ["bagpipes", "banjo", "accordion"],
    "weather phenomena": ["blizzard", "tornado", "hurricane"],
    "animals": ["dog", "cat", "elephant"]
}

# Randomly select a category and a word from that category
category, words = rand.choice(list(word_categories.items()))
word_to_be_guessed = rand.choice(words)

print(f"The word is from the category: {category}")
print("The length of the word is ", len(word_to_be_guessed))
# Maximum chances before game over
maximum_chances = 3

# Counter for incorrect guesses
wrong_words_counter = 0

# List to track guessed letters
lst_of_guessed_words = []

# Function to display the current state of the word
def display_word_state(word, guessed_letters):
    # Display each letter if guessed, otherwise an underscore
    return "".join([letter if letter in guessed_letters else "_" for letter in word])

# While loop with dynamic control
current_guess = 0
total_guesses = len(word_to_be_guessed)

while current_guess < total_guesses:
    # Display current word state, incorrect guesses, and chances left
    print("Current word state:", display_word_state(word_to_be_guessed, lst_of_guessed_words))
    print("Incorrect guesses:", wrong_words_counter)
    print("Chances left:", maximum_chances - wrong_words_counter)

    # Get user input and ensure it's a single alphabetic letter
    guess = input("Guess a letter: ").strip().lower()
    
    if not guess.isalpha() or len(guess) > 1:
        print("Please enter a single alphabetic letter.")
        continue  # Prompt the user again
    
    if guess in lst_of_guessed_words:
        print("You already guessed this letter 😊")
        total_guesses += 1  # Allow retrying
    
    elif guess in word_to_be_guessed:
        # Check how many times the guessed letter appears in the word
        count_in_word = word_to_be_guessed.count(guess)

        # Add the guessed letter to the list the correct number of times
        for _ in range(count_in_word):
            lst_of_guessed_words.append(guess)

        # Check if all unique letters have been guessed
        unique_guessed_letters = set(lst_of_guessed_words)
        unique_letters_in_word = set(word_to_be_guessed)

        if unique_guessed_letters == unique_letters_in_word:
            print("Congratulations! You've guessed the word:", word_to_be_guessed)
            break

        current_guess += 1  # Move to the next guess
    
    elif guess not in word_to_be_guessed:
        print("You guessed a wrong letter!")
        wrong_words_counter += 1
        if wrong_words_counter == maximum_chances:
            print("Game over")
            break

print("The letter to be guessed is ", word_to_be_guessed)


