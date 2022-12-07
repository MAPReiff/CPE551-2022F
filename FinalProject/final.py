# I pledge my honor that I have abided by the Stevens Honor System.

# This program is a game of War. Rules are based on the Bicycle Cards website.
# https://bicyclecards.com/how-to-play/war/

# Rules/Info
# War is typically played with a standard 52-card deck. The cards are divided evenly
# between two players. In this case, it will be the user and the computer. Each player
# then plays the top card from their deck. The player with the higher card rand takes
# both cards and adds them to the bottom of their deck. If the cards are the same rank,
# then there is a war. Both players place the next card of their deck face down and then
# another card face up. The player with the higher card takes all six cards and adds them
# to the bottom of their deck. If the cards are the same rank, then the war repeats until
# one player has a higher card. The game ends once one player has won all the cards.

import time  # Used for the countdown timer function
import random  # Used for the random card generator

# This clsss is based on code from Stack Overflow, making it easier to print in different
# colors to better distinguish between the human and the computer, and other important lines
# of text.
# https://stackoverflow.com/a/17303428


class color:
    HUMAN = '\033[95m'
    COMPUTER = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'


# From lecture 9
######################################################################

class Card:
    suit_list = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_list = ["None", "Ace", "2", "3", "4", "5", "6", "7",
                 "8", "9", "10", "Jack", "Queen", "King"]  # ignoring Joker

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # the blank of blank
        return (self.rank_list[self.rank] + " of " + self.suit_list[self.suit])

    def __eq__(self, other):
        # are the suits and ranks the same?
        return (self.suit == other.suit and self.rank == other.rank)

    def __gt__(self, other):
        if self.suit > other.suit:  # if a suit is greater than another suit
            return True
        elif self.suit == other.suit:  # if the suits are the same
            if self.rank > other.rank:  # if the rank is greater than the other rank
                return True
            else:  # if the rank is less than or equal to the other rank
                return False
        else:  # if the suit is less than the other suit
            return False


class Deck:
    def __init__(self):  # initialize the deck
        self.cards = []  # empty list
        for suit in range(4):  # for each suit
            for rank in range(1, 14):  # for each rank
                self.cards.append(Card(suit, rank))  # add a card to the deck

    def __str__(self):  # print the deck
        s = ""  # empty string
        for i in range(len(self.cards)):  # for each card in the deck
            # add the card to the string
            s += i * " " + str(self.cards[i]) + "\n"
        return s

    def shuffle(self):  # shuffle the deck
        n_cards = len(self.cards)  # number of cards in the deck
        for i in range(n_cards):  # for each card in the deck
            # pick a random card to swap with
            j = random.randrange(i, n_cards)
            # swap the cards
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def pop_card(self):
        return self.cards.pop(-1)

    def is_empty(self):
        return len(self.cards) == 0

    def deal(self, players, n_cards=52):
        n_players = len(players)  # number of players
        for i in range(n_cards):  # for each card
            if self.is_empty():  # if the deck is empty
                break  # break out of the loop
            card = self.pop_card()  # take the top card
            current_player = i % n_players  # find the current player
            # add the card to the player's hand
            players[current_player].add_card(card)


class Hand(Deck):
    def __init__(self, name=""):
        self.cards = []  # empty list
        self.name = name  # name of the hand

    def add_card(self, card):  # add a card to the hand
        self.cards.append(card)  # add the card to the list

    def __str__(self):  # print the hand
        s = "Hand " + self.name  # start with the name of the hand
        if self.is_empty():  # if the hand is empty
            return s + " is empty\n"  # return a string indicating that the hand is empty
        s += " contains\n" + Deck.__str__(self)  # add the cards in the hand
        return s

    def shuffle(self):  # shuffle the player's hand
        n_cards = len(self.cards)  # number of cards in the hand
        for i in range(n_cards):  # for each card in the hand
            # pick a random card to swap with
            j = random.randrange(i, n_cards)
            # swap the cards
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
            # I added this in to help solve a bug that occurs when a user wins
            # a card, that card is what would be played next. As War does not
            # depend on card order, I will shuffle each player's hand between
            # rounds to minimize the chance of this happening.

############################################################################################################


print("Welcome to War! Let's get started!\n")

# Ask player for their name
# playerName = ("Human")
playerName = input("Please tell me your name: ")


# Create a hand for the player and the computer
human = Hand(playerName)
computer = Hand("Computer")
players = [human, computer]

# Create a deck, shuffle it and deal it to the players
d = Deck()
d.shuffle()
d.deal(players, 52)

# Print each player's hand (for testing purposes)
# print(human)
# print(computer)

# Function to have a countdown before the next round based on code from
# https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/


def roundCountdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("The next round will begin in", timer, end="\r")
        time.sleep(1)
        seconds -= 1
    # This string must be longer than the timer string
    print('                                       ')


# Needed vars
round = 0  # Round counter
gameOver = False  # Game over flag
timer = 2  # seconds
wins = [0, 0]  # Wins for each player
warWins = [0, 0]  # War wins for each player
warTies = 0  # War ties
wars = 0  # Number of wars

# The game itself is a loop, which does not end till the game is won
while gameOver != True:
    round += 1
    print(color.BLUE + "~~~~~~~~~~ Round",
          str(round) + " ~~~~~~~~~~" + color.END)

    # Each player plays the top card from their deck
    humanCard = human.pop_card()
    computerCard = computer.pop_card()
    print(color.HUMAN + playerName + " played the",
          color.BOLD + str(humanCard) + color.END)
    print(color.COMPUTER + "The computer played the",
          color.BOLD + str(computerCard) + color.END + "\n")

    # Compare the played cards
    if humanCard.rank > computerCard.rank:  # Human wins and gets both cards
        wins[0] += 1
        print(color.HUMAN + playerName + " wins this round!" + color.END + "\n")
        human.add_card(humanCard)
        human.add_card(computerCard)
    elif humanCard.rank < computerCard.rank:  # Computer wins and gets both cards
        wins[1] += 1
        print(color.COMPUTER + "The computer wins this round!" + color.END + "\n")
        computer.add_card(humanCard)
        computer.add_card(computerCard)
    else:  # War!
        wars += 1
        print(color.BOLD + color.RED +
              playerName + " and the computer have tied! It's time for a war!" + color.END + "\n")
        war = True  # Set war to true so we can start a war loop
        # Create a list to hold the cards played during the war, starting with the initial cards
        warCards = [humanCard, computerCard]

        while war == True:
            # If either player is out of cards, the game is over as there is no way to play a war
            if human.is_empty():
                warWins[1] += 1  # Computer wins the war
                for card in warCards:
                    computer.add_card(card)
                war = False
                gameOver = True
                print(color.BOLD + color.RED +
                      playerName + "is out of cards! Unable to wage war!" + color.END + "\n")
                break
            elif computer.is_empty():
                warWins[0] += 1  # Human wins the war
                for card in warCards:
                    human.add_card(card)
                war = False
                gameOver = True
                print(color.BOLD + color.RED +
                      "The computer is out of cards! Unable to wage war!" + color.END + "\n")
                break

            # If either player has less than 2 cards, they can't play a war either
            if len(human.cards) < 2:
                warWins[1] += 1  # Computer wins the war
                for card in human.cards:  # Add all of the human's remaining cards to the war pile
                    cards = human.pop_card()
                    warCards.append(cards)
                for card in warCards:  # Add all of the cards in the war pile to the computer's deck
                    computer.add_card(card)
                war = False
                gameOver = True
                print(color.BOLD + color.RED +
                      playerName + " does not have enough cards to wage war!" + color.END + "\n")
                break
            elif len(computer.cards) < 2:
                warWins[0] += 1  # Human wins the war
                for card in computer.cards:  # Add all of the computer's remaining cards to the war pile
                    cards = computer.pop_card()
                    warCards.append(cards)
                for card in warCards:  # Add all of the cards in the war pile to the human's hand
                    human.add_card(card)
                war = False
                gameOver = True
                print(color.BOLD + color.RED +
                      "The computer does not have enough cards to wage war!" + color.END + "\n")
                break

            # Play the next two cards, one as a sacrifice and one to play
            humanSacrifice = human.pop_card()
            computerSacrifice = computer.pop_card()
            humanWarCard = human.pop_card()
            computerWarCard = computer.pop_card()
            print(color.HUMAN + playerName + " played the",
                  color.BOLD + str(humanWarCard) + color.END)
            print(color.COMPUTER + "The computer played the",
                  color.BOLD + str(computerWarCard) + color.END + "\n")

            # Add all of the cards played during the war to the warCards list
            warCards.append(humanWarCard)
            warCards.append(computerWarCard)
            warCards.append(humanSacrifice)
            warCards.append(computerSacrifice)
            if humanWarCard.rank > computerWarCard.rank:  # Human wins the war
                warWins[0] += 1
                print(playerName + " won the war!")
                for card in warCards:  # Add all of the cards in the war pile to the human's hand
                    human.add_card(card)
                war = False
            elif humanWarCard.rank < computerWarCard.rank:  # Computer wins the war
                warWins[1] += 1
                print("The computer won the war!")
                for card in warCards:  # Add all of the cards in the war pile to the computer's hand
                    computer.add_card(card)
                war = False
            else:  # War results in a tie and thus continues the loop
                warTies += 1
                print(color.RED + color.BOLD +
                      playerName + " and the computer have tied again! It's time for another war!" + color.END)

    # Print the number of cards each player has
    print(color.HUMAN + playerName + " has", len(human.cards),
          "cards left in their hand." + color.END)
    print(color.COMPUTER + "The computer has", len(computer.cards),
          "cards left in its hand." + color.END + "\n")

    # Check if either the human or the computer has won/lost the game
    if human.is_empty() == True:
        print(color.YELLOW + playerName + "have run out of cards." + playerName + "is the " +
              color.BOLD + "loser!" + color.END + "\n\n")
        gameOver = True
        break
    elif computer.is_empty() == True:
        print(color.YELLOW + "The computer has run out of cards." + playerName + "is the the " +
              color.BOLD + "winner!" + color.END + "\n\n")
        gameOver = True
        break
    
    # Shuffle player hands
    human.shuffle()
    computer.shuffle()

    # Timer for the next round
    roundCountdown(timer)

# Print final stats
print(color.BOLD + color.YELLOW + "Final Stats:" + color.END)
print(color.BOLD + color.BLUE + "There were " +
      str(round) + " total rounds." + color.END)
print(color.BOLD + color.RED + "There were " + str(wars) + " wars." + color.END)
print(color.BOLD + color.RED + "There were " +
      str(warTies) + " tied wars." + color.END)
print(color.BOLD + color.HUMAN + playerName + " won " +
      str(wins[0]) + " rounds, and " + str(warWins[0]) + " wars!" + color.END)
print(color.BOLD + color.COMPUTER + "The computer won " +
      str(wins[1]) + " rounds, and " + str(warWins[1]) + " wars!" + color.END)

# The end
