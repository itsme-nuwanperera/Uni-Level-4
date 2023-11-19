import json
import math
import random


welcome_msg = """
Guess the word

Select Level:
    1) Eazy       : Unlimited turns
    2) Medium     : Word length + extra 4 turns
    3) Hard       : Word length

"""

#
def load_data(path: str="tut-5/guess_the_word/words.json") -> dict:
  try:
    with open(path, "r") as f:
      data = json.load(f)
      return data
  
  except FileNotFoundError:
    print("Can't read word file!")
    exit()
  
#
def get_level():
  user_choice = input("Enter the number (q -> exit): ").lower()
  print()

  if (user_choice == "q"):
    exit()
  else:
    try:
      user_choice = int(user_choice)
      if (user_choice in range(1,4)):
        return user_choice
      
    except ValueError:
      print("Please Enter the choice number!")
    return get_level()

#
def select_word(level: int, words_set: dict) -> str:
  lst = words_set.get("eazy")
  match level:
    case 1:
      lst = words_set.get("eazy")
    case 2:
      lst = words_set.get("medium")
    case 3:
      lst = words_set.get("hard")

  return random.choice(lst)

#
def print_guessing_word(char_list: list):
  print("  ".join(char_list))

#
def get_guesses():
  letter = input("Enter your guessing letter (a-z): ").lower()
  if (letter == "" or len(letter) != 1):
    return get_guesses()
  return letter

# 
def is_valid_letter(letter: str, word: str) -> bool:

  return (letter in word)

def is_word_done(lst):
  return "_" in lst

def get_retry_count(lvl: int, word: str):
  match (lvl):
    case 1:
      return math.inf
    case 2:
      return len(word) + 4
    case 3:
      return len(word)
    

def main():  
  content = load_data()

  print(welcome_msg)

  level = get_level()
  word = select_word(level, content)
  retry_count = get_retry_count(level, word)

  empty_char_list = ["_" for _ in word]

  while (is_word_done(empty_char_list) and retry_count > 0):
    print_guessing_word(empty_char_list)
    char = get_guesses()

    if (not is_valid_letter(char, word)):
      retry_count -= 1
      print("Try again!")
      continue
    print("You guessed correct!")
    for i, c in enumerate(word):
      if (c == char):
        empty_char_list[i] = c

  print(f"{word}\nYou guessed the whole word correctly!")
    


main()