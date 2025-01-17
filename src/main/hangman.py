import random 

word_list = ["beekeper", "geek", "orange", "order", "software"]

chosen_word = word_list[random.randint(0, len(word_list) -1)]

guess = ["_"]*len(chosen_word)

print(chosen_word)
guessed_char  = input("Guess a letter: ").lower()


for i in range(len(chosen_word)):
    if chosen_word[i] == guessed_char:
        guess[i] = guessed_char
        
print(guess)