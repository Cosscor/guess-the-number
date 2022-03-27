from random import randint
easy_level = 10
hard_level = 5

def check_answer(guess, answer, turns):
  if guess > answer:
    print("To hight")
    return turns -1
  elif guess < answer:
    print("To low")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def set_difficulty():
  level = input("Chose a difficulty. Type 'easy', or 'hard': ")
  if level == 'easy':
    return easy_level
  else:
    return hard_level
def game():
  print("Welcom to the Number Guesing Game")
  print("I'm thimking of a number between 1 and 100.")
  answer = randint(1, 100)
  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attemps remaining to guess the number")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've rune out of guesses, you lose.")
    elif guess != answer:
      print("Guess again. ")
game()   
    
  
  
  
  

