#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
#importing functions
import random
from art import logo,win,loss,bye
from replit import clear
#random number Generator
def number_selector():
  return random.randint(0,100)
def game():
  #creating a function for easy and hard
  def easy_and_hard(num,select):
    if select =="hard":
      selected=5
    else:
      selected=10
    counter=selected
    while counter >0:
      user_number=int(input("enter your number:->"))
      print(f"You have {counter} tries")
      if user_number == num:
        print(f"The guess is correct. \nThe number is {num} \n YOU WIN")
        counter=0
        print(win)
      elif user_number > num:
        print("Too high")
        counter -= 1
      else:
        print("Too low")
        counter -= 1
    if counter ==0:
      print(f"Your tries finished.\n The number is {num}")
      print(loss)




  #main programme
  print(logo)
  print("***********Welcome to the game***********")
  difficulty=input("Select your difficulty level-Hard or Easy\n").lower()
  easy_and_hard(number_selector(),difficulty)
  if input("Do you want play again? yes or no\n").lower() =="yes":
    clear()
    game()
  else:
    
    clear()
    print(bye)

game()