"""Deck Tests"""
from deck import Deck
from card import Card


def test_creation():
    """Test if decks of cards were created correctly"""
    my_deck = Deck()
    assert len(my_deck.cards) == 52


def test_deck():
    """Test if there are 13 cards of each type"""
    my_deck = Deck()
    cards = [(card.value, card.color) for card in my_deck.cards]
    print(cards)

    for color in Card.possible_colors.values():
        # # tu numerek bo to jest tupla a nie obiekt 1 -> color
        # heart_cards = [card for card in cards if card[1] == '\u2661']
        # assert len(heart_cards) == 13

        #  wersja sprawdzenia wszytskich kolorów na raz
        for color in Card.possible_colors.values():
            cards_in_color = [card for card in cards if card[1] == color]
            assert len(cards_in_color) == 13


def test_shuffle():
    """Test whether to shuffle the cards correctly"""
    my_deck = Deck()
    # : oznacza skopiowanie listy kart do nowej zmiennej, bez tego zawsze mamy wskaźnik na tą samą rzecz
    cards = my_deck.cards[:]
    my_deck.shuffle()
    assert cards != my_deck.cards


def test_deck_hit():
    """Test if the drawn card is the last one in the deck"""
    my_deck = Deck()
    last_card = my_deck.cards[-1]
    hitted_card = my_deck.hit()
    assert last_card == hitted_card


def test_deck_count_card():
    """Test whether the drawn card is removed from the deck"""
    my_deck = Deck()
    card = my_deck.hit()
    assert len(my_deck.cards) == 51
    assert card not in my_deck.cards
