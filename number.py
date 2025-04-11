import random

def guess(y):
  random_number = random.randint(1,y)
  guess = 0
  while guess != random_number:
    guess = int(input(f"Guess a number between 1 and {y}: "))
    if guess < random_number:
      print("Sorry guess again. Too low")
    elif guess > random_number:
     print("Sorry guess again. Too high")
    else:
      print("yay you got it.")
      print(guess)

guess(10) 