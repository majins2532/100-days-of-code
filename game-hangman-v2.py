### Game Hangman
import random

hanged_man = [
        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]

data = ["hangman","production"]
chosen_word = random.choice(data)

display = ["_"]*len(chosen_word)
continue_game = len(hanged_man)-1
#print(f"HANGMAN = {chosen_word} and continue_game : {continue_game}")

while "_" in display and continue_game:
    guess = input("Guess a letter:").lower()
    wrong = False
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
            wrong = True
    if not wrong:
        continue_game -= 1
        print(hanged_man[(len(hanged_man)-1)-continue_game])
    print(f"{display} and continue = {continue_game}")
            
if continue_game:
    print("Your Won.")
else:
    print("Your Dead.")
