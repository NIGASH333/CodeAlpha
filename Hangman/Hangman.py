import random
def choose_word():
    words=["apple","banana","orange","grape","pineapple","strawberry"]
    return random.choice(words)
def display_word(word,guessed_letters):
      display=""
      for letter in word:
            if letter in guessed_letters:
                  display+=letter+""
            else:
                  display+="_"
      return display
def hangman():
      word=choose_word()
      guessed_letters=[]
      incorrect_guesses=0
      max_attempts=6
      print("Welcome to Hangman!")
      print(display_word(word,guessed_letters))
      
      while True:
            guess=input("Guess a letter:").lower()

            if guess in guessed_letters:
                  print("you've already guessed that letter!")
                  continue
            guessed_letters.append(guess)

            if guess in word:
                  print("Correct guess!")
            else:
                  incorrect_guesses+=1
                  print("incorrect guess!")
                  print(f"Remaining attempts:{max_attempts-incorrect_guesses}")
            print(display_word(word,guessed_letters))

            if all(letter in guessed_letters for letter in word):
                  print("Congratulations! You guessed the word correctly!")
                  break
            elif incorrect_guesses==max_attempts:
                  print("Sorry,you've run out of attempts.The word was:",word)
                  break
hangman()
                  
