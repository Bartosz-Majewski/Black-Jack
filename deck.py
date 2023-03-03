"""Deck description"""
from random import shuffle
from card import Card


class Deck:
    def __init__(self):
        """creating a deck of cards"""
        self.cards = []
        for color in Card.possible_colors:
            for value in Card.possible_values:
                self.cards.append(
                    Card(color=color, value=value)
                )

    def shuffle(self):
        """shuffle a deck"""
        shuffle(self.cards)

    def hit(self):
        """drawn card"""
        return self.cards.pop()


deck = Deck()
