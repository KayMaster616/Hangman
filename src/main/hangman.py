import random 
from hangman_words import word_list as words
from hangman_art import logo as logo, stages as stages


chosen_word = random.choice(words)

display = ["_"]*len(chosen_word)

# print(chosen_word)

end_of_game = False

count_chars = len(display)
current_chars = count_chars
lives = 6
print(logo)
while not end_of_game:
    
    guessed_char  = input("Guess a letter: ").lower()

    if guessed_char in display:       
        
        print("You already guessed this letter")
                
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
                print(f"The word was - {chosen_word}")
  
    print(" ".join(display))        
    print(stages[lives])        
    
