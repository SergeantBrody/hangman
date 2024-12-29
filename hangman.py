import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
chosen_word_list = []
for char in chosen_word:
    chosen_word_list.append(char)


display_list = []

for char in chosen_word:
    display_list.append('_')

display_word = ''

for element in display_list:
    display_word += element

print(display_word)
errors = 0
while '_' in display_list:
    
    guess = input("Guess the letter: ").lower()
    if guess in display_list:
        print(f"You already guessed this letter: {guess}")
    elif guess in chosen_word_list:
        indices = [index for index, value in enumerate(chosen_word_list) if value == guess]
        
        for index in indices:
            display_list[index] = guess
        display_word = ''
        for element in display_list:
            display_word += element
        print(display_word)
        print("CORRECT !")
    else:
        print(f"{guess} not in word !")
        print(HANGMANPICS[errors])        
        if errors == (len(HANGMANPICS) - 1):
            print("you lose : (")
            print(f"The word was: {chosen_word}")
            break
        errors += 1
if '_' not in display_list:
    print(f"You have won ! The word was: {chosen_word}")