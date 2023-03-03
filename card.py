"""BlackJack ASCII Python game
    Description for card"""
from exceptions import InvalidColor, InvalidValue


class Card:
    """Card abstarction"""
    # użycie zmiennych statycznych - takie coś uniemożliwia przesłanie innych kolorów niz te zadeklarowane tutaj
    possible_colors = {
        'spades': '\u2664',
        'diamonds': '\u2662',
        'hearts': '\u2661',
        'clubs': '\u2667'
    }

    possible_values = list(range(2, 11)) + [
        'Ace',
        'Jack',
        'Quenn',
        'King'
    ]

    def __init__(self, color, value) -> None:
        if color not in self.possible_colors:
            raise InvalidColor('Invalid color!!')

        self.color = self.possible_colors[color]

        if value not in self.possible_values:
            raise InvalidValue('Invalid card value')

        self.value = value

    def __repr__(self) -> str:
        return f'{self.value} -> {self.color}'
