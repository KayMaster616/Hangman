import random 

word_list = ["beekeper", "geek", "orange", "order", "software"]

chosen_word = word_list[random.randint(0, len(word_list) -1)]

guess = ""
print(chosen_word)
guessed_char  = input("Guess a letter: ")


for letter in chosen_word:
    if letter == guessed_char:
        print("Right")
        
    else:
        print("Wrong")