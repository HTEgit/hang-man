from words import words
import random
import string

def get_valid_word(words):
    word=random.choice(words)
    while ' ' in words or '-' in words:
        word = random.choice(words)
    return word.upper()
def hangman():
    word=get_valid_word(words)
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()
    lives=6
    while len(word_letters)>0 and  lives>0:
      print(" u are left with",lives,"lives and used letters are",' '.join(used_letters))
      word_list=[letter if letter in used_letters else '-' for letter in word]
      print("current word:",' '.join(word_list))
      user_input=input("Guess the word: ")
      if user_input in alphabet-used_letters:
        used_letters.add(user_input)
        if user_input in word_letters:
          word_letters.remove(user_input)
        else:
            lives-=1
            print("the letter u guessed is not in the word")
      elif user_input in used_letters:
            print("opps u have used the letter already")
      else:
            print("opps u have wrong input")
    if lives==0:
        print("opps u lost the word was",word)
    else:
        print("congrats, u have won")
hangman()

