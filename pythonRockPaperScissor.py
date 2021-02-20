#Rock paper scissors game
import random

def  play():
  user = input("What's your choice? 'r' for Rock, 'p' for Paper, 's' for Scissors\n")
  computer = random.choice(['r', 'p', 's'])

  if user == computer:
    return "It\'s tie"
  
  # r> s, s > p, p > r
  if is_win(user, computer):
    return 'You won!'

  return 'You lost'

def is_win(player, opponent):
  #retirn true if player wins 
  # r> s, s > p, p > r
  if (player == 'r' and opponent == 's') or (player == 's' and 'p') or (player == 'p' and opponent == 'r'):
    return True

print(play())

print(f'\n\nThanks for playing my Rock, Paper, Scissors Game! Checkout some of my other stuff at tylerlorenzen.tech! \n\nThanks,\n\nTyler!')
