import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

game_over = False
lives = 6

print(logo)

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}.")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word.")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        game_over = True
        print("You win!")

    print(stages[lives])
