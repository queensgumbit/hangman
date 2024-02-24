import random

from hangmanWords import word_list

random_word = random.choice(word_list)

display = []

from hangmanArt import logo
print(logo)

for i in range(len(random_word)):
    display+='_'
print(display)
lives = 6

end_of_game = False #still not the end of the game

while not end_of_game:
    try:
        user_guess = input('guess a letter: ').lower()
    except ValueError:
        print('you have entered wrong value,possibly a number')

    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == user_guess:
            display[position] = letter
    if user_guess not in random_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('you lost...')

    print(lives)
    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print('you won !')

    from hangmanArt import stages

    print(stages[lives])
