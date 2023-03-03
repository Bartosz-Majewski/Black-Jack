"""player description"""
from card import Card
from exceptions import GameOverException


class Player:
    def __init__(self) -> None:
        self.cards = []

    def take_card(self, card: Card):
        """a player draws a card from the deck"""
        self.cards.append(card)

    def calculate_points(self):
        """a method for counting points scored by a player"""
        points = 0

        # How many aces do we have ?
        number_of_aces = len(
            [card for card in self.cards if card.value == 'Ace'])

        if number_of_aces == 2 and len(self.cards) == 2:
            return 21

        if number_of_aces == 1 and len(self.cards) == 2:
            points = 10

        for card in self.cards:
            if card.value == 'Ace':
                points += 1
            elif card.value in ['Ace', 'Jack', 'Quenn', 'King']:
                points += 10
            else:
                points += card.value

        # druga wersja tego samego
        # for card in self.cards:
        #     try:
        #         points += int(card.value)
        #     except ValueError:
        #         points += 10

        if points > 21:
            raise GameOverException('Number of points exceeded!')
        return points
