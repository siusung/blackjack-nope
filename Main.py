"""
BlackJack
Started on 8/22/2020
Trying to get back into the groove of coding and build some confidence that I can make my own project!
"""

import random
import os

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}


def main():

    while True:
        print("\nNew Game: BLACK JACK\n")
        game_deck = Deck()
        game_deck.shuffle()

        player_name = str(input("Name your player: "))
        player = Player(player_name)
        dealer = Dealer()

        if ready():
            pass

        os.system('cls')



        for i in range(0, len(game_deck.all_cards)):
            print(game_deck.all_cards[i])


        if not replay():
            break

def replay():
    choice = None
    while choice not in ["y", "n"]:
        choice = input("Play again? [y/n]: ").lower()
    if choice == "y":
        return True
    elif choice == "n":
        return False

def ready():
    choice = None
    while choice not in ["y", "n"]:
        choice = input("Ready to play? [y/n]: ")
    if choice == "y":
        return True
    elif choice == "n":
        return False


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank.capitalize()]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Hand:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def check_value(self):
        value = 0
        for card in self.hand:
            value += card.value

        return value


class Player:
    def __init__(self, name):
        self.win_status = None
        self.name = name
        self.player_hand = Hand()
        self.bankroll = 100.00

    def bet(self, bet_amount):
        if bet_amount <= self.bankroll:
            self.bankroll -= bet_amount
            return bet_amount
        return -1


class Dealer:
    def __init__(self):
        self.win_status = None
        self.dealer_hand = Hand()


if __name__ == '__main__':
    main()
