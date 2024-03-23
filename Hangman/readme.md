# Hangman Game

![Screenshot (12)](https://github.com/NIGASH333/CodeAlpha/assets/113447646/0d622624-9eea-49da-a282-e34dd55a99ea)


This is a simple Hangman game implemented in Python. The game randomly selects a word from a predefined list, and the player must guess the letters in the word within a limited number of attempts.

## How to Play

1. **Run the script**: Execute the Python script to start the game.

2. **Guess the letters**: Enter letters one at a time to guess the word. If the letter is correct, it will be revealed in the word. If incorrect, the number of remaining attempts will decrease.

3. **Win or Lose**: Keep guessing letters until you either guess the word correctly or run out of attempts.

4. **End of Game**: The game ends when either the word is guessed correctly or the player runs out of attempts.

## Program Structure

- **choose_word()**: Selects a random word from a predefined list.
- **display_word(word, guessed_letters)**: Displays the word with guessed letters revealed and underscores for unguessed letters.
- **hangman()**: Main function to control the game flow, including handling user input, checking guesses, and determining the game's outcome.

## Game Rules

- The player has a limited number of attempts to guess the word.
- Correctly guessed letters are revealed in the word.
- Incorrect guesses decrease the remaining attempts.
- The game ends when the word is guessed correctly or the player runs out of attempts.

## Dependencies

- Python 3.x

## Acknowledgments

This Hangman game implementation is based on a simple Python tutorial.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
