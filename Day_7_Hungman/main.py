import random
import hungman_art as man
from words import words 
lives = 6

print(man.welcome)
print(man.logo)
chosen_word = random.choice(words)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"***************************** {lives}/6 LIVES LEFT ********************************")
    guess = input("Guess the letter for completing the word.\n").lower()
    if guess in correct_letters:
        print(f"You have already guessed this letter {guess}.")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    print("Words to guess: "+ display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"**************** IT WAS {chosen_word} YOU LOSE ********************")
        else:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")

    if "_" not in display:
        game_over = True
        print("**************** YOU WIN ********************")
    
    print(man.stages[lives])
    