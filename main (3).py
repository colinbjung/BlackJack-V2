# Author: Colin
# Python-based imitation of blackjack

import random
from art import logo
from replit import clear

# Function prompts user to play blackjack
def want_to_play():
  while(input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == 'y'):
    blackjack()
 
# Function selects random cards from 
def blackjack():
  user_cards = []
  computer_cards = []
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  user_cards.append(random.choice(cards)) # Dealing cards
  computer_cards.append(random.choice(cards))
  user_cards.append(random.choice(cards))
  computer_cards.append(random.choice(cards))
  clear()
  print(logo)
 
  continue_game = True
  while(continue_game):
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"\tYour cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"\tComputer's first card: {computer_cards[0]}")
    if computer_score == 0:
      continue_game = False
    elif user_score == 0:
      continue_game = False
    elif user_score > 21:
      continue_game = False
    else:
      user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_choice == 'y':
        user_cards.append(random.choice(cards))
      else:
        continue_game = False

  while computer_score < 17 and computer_score != 0:
    computer_cards.append(random.choice(cards))
    computer_score = calculate_score(computer_cards)

  print(f"\tYour final hand: {user_cards}, final score: {user_score}")
  print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")
  print(winner(user_score, computer_score))

  # ask if you want to draw
  
def calculate_score(cards):
  total_score = sum(cards)
  if total_score == 21 and len(cards) == 2:
    return 0
  # for lists you can say "x in list_variable" == list contains x 
  if total_score > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
    total_score = sum(cards)
  return total_score

def winner(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack"
  elif user_score == 0:
    return "Blackjack, you win"
  elif user_score > 21:
    return "You went over. You lose"
  elif computer_score > 21:
    return "Opponent went over. You win"
  elif user_score > computer_score:
    return "You win"
  elif computer_score > user_score:
    return "You lose"
  

want_to_play()