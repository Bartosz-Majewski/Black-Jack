"""Card tests"""

from card import Card, InvalidColor, InvalidValue
import pytest


def test_creation():
    """Test if I can create valid card"""
    card = Card('hearts', 'Ace')
    print(card.value)  # aby się wyświetliło należy po pytest dodać -s
    assert card.color == '\u2661'
    assert card.value == 'Ace'


def test_creation_wrong_value():
    """Test if code raises exception when wrong value"""
    # łapanie błedu, jeśli wystąpi ten bład test przejdzie
    with pytest.raises(InvalidValue) as message:
        Card('hearts', 'A')
        assert message == 'Invalid card value'


def test_creation_wrong_color():
    """Test if code raises exception when wrong color"""
    with pytest.raises(InvalidColor) as message:
        Card('xyz', 'A')
        assert message == 'Invalid card value'


def test_card_represantation():
    """Test if card has correct card represantion"""
    # można tak ale i tak
    # card = Card('hearts', 'Ace')
    # assert repr(card) == 'Ace -> \u2661'
    assert repr(Card('hearts', 'Ace')) == 'Ace -> \u2661'
    assert repr(Card('diamonds', 'Ace')) == 'Ace -> \u2662'
    assert repr(Card('spades', 'Ace')) == 'Ace -> \u2664'
    assert repr(Card('clubs', 'Ace')) == 'Ace -> \u2667'
