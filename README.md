# Hangman Game

Welcome to the Hangman Game! This is a simple and fun Python implementation of the classic word-guessing game, where you try to guess a hidden word one letter at a time before running out of lives.

---

## Features
- **Random Word Selection**: Words are randomly chosen from a predefined list.
- **ASCII Art**: Visual stages of the hangman game are displayed for an engaging experience.
- **Input Validation**: Ensures valid guesses (single letters) and provides feedback for repeated guesses.
- **Win/Loss Feedback**: Displays the correct word at the end of the game.

---

## How to Play
1. Clone this repository to your local machine.
2. Ensure you have Python installed (version 3.x).
3. Run the `hangman.py` script using the following command:
   ```bash
   python hangman.py
   ```
4. Follow the prompts to guess letters. Try to guess the hidden word before the hangman drawing is completed!

---

## Project Structure
The project consists of the following files:

- **hangman.py**: The main script containing the game logic.
- **hangman_words.py**: A module containing a list of words for the game.
- **hangman_art.py**: A module with the ASCII art for the hangman stages and the game logo.

---

## Sample Output
```
Welcome to Hangman!

+---+
|   |
    |
    |
    |
    |
=====

_ _ _ _ _

Guess a letter: a

_ _ a _ _

+---+
|   |
    |
    |
    |
    |
=====

Guess a letter: e
Your guess is wrong.

+---+
|   |
O   |
    |
    |
    |
=====

_ _ a _ _
```

---

## Enhancements
### Planned Features
- Difficulty Levels: Choose between easy, medium, and hard.
- Hint System: Allow players to request a hint at the cost of a life.
- Replay Option: Add the ability to restart the game without exiting.

---

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions or improvements.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
- ASCII art and word lists inspired by the Python community.
- Created for educational purposes and for anyone who loves classic games.

---

Enjoy playing Hangman! Happy guessing!

