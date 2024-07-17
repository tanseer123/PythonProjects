import random
# List of words for the game
words = ["apple", "banana", "cherry", "orange", "grape", "pear"]
# Function to choose a random word from the list
def choose_word():
    return random.choice(words)
 # Function to play the hangman game
def play_hangman(word):
    guessed_letters = []
    attempts = 6
    while attempts > 0:
        word_masked = ''.join(letter if letter in guessed_letters else '_' for letter in word)
        print("Word:", word_masked)
        if '_' not in word_masked:
            print("Congratulations! You guessed the word correctly.")
            break
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts remaining.")
        else:
            print("Sorry, you ran out of attempts. The word was:", word)
 # Main program
if __name__ == "__main__":
    word_to_guess = choose_word()
    print("Welcome to Hangman!")
    play_hangman(word_to_guess)