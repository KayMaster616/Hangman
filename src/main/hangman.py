import random 

word_list = ["beekeper", "geek", "orange", "order", "software"]

chosen_word = word_list[random.randint(0, len(word_list) -1)]

display = ["_"]*len(chosen_word)

print(chosen_word)

end_of_game = False

while not end_of_game:
    guessed_char  = input("display a letter: ").lower()


    for i in range(len(chosen_word)):
        if chosen_word[i] == guessed_char:
            display[i] = guessed_char
            
    print(display)
    
    if "_" not in display:
        end_of_game = True
    
    
    
print("You win!")