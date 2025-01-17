import random 

word_list = ["beekeper", "geek", "orange", "order", "software"]

chosen_word = word_list[random.randint(0, len(word_list) -1)]

display = ["_"]*len(chosen_word)

print(chosen_word)

end_of_game = False

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# print(stages[5])

count_chars = len(display)
current_chars = count_chars
lives = 6
while not end_of_game:
    
    guessed_char  = input("display a letter: ").lower()

    if guessed_char in display:
            
        lives -= 1
        print("You already guessed this letter")
        if lives == 0:
            end_of_game = True
            print("Sorry, You lost!")
                
    else:
    
        for i in range(len(chosen_word)):
            if chosen_word[i] == guessed_char:
                display[i] = guessed_char
                
        if guessed_char in chosen_word:
            
            if "_" not in display:
                end_of_game = True
                print("Congrats, You win!")
        
        else:
            lives -= 1
            print("Your guess is wrong")
            if lives == 0:
                end_of_game = True
                print("Sorry, You lost!")
  
    print(" ".join(display))        
    print(stages[lives])        
    
