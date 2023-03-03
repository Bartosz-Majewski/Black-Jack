"""tests for player methods"""
from player import Player
from card import Card


def test_calculate_player_points():
    """test if the method correctly counts the number of points scored by the player"""
    # given
    card = Card('spades', 2)
    card2 = Card('hearts', 5)
    player = Player()

    # when
    player = Player()
    player.take_card(card)
    player.take_card(card2)

    # then
    assert player.calculate_points() == 7


def test_calculate_player_points_two_aces():
    """test if the method correctly counts the number of points scored by the player 
    when the player drew two aces in the first draw"""
    # given
    card = Card('spades', 'Ace')
    card2 = Card('hearts', 'Ace')
    player = Player()

    # when
    player = Player()
    player.take_card(card)
    player.take_card(card2)

    # then
    assert player.calculate_points() == 21


def test_calculate_player_points_one_ace_two_cards():
    """test if the method correctly counts the number of points scored by the player 
    when the player drew one ace in the first draw"""
    # given
    card = Card('spades', 'Ace')
    card2 = Card('hearts', 2)
    player = Player()

    # when
    player = Player()
    player.take_card(card)
    player.take_card(card2)

    # then
    assert player.calculate_points() == 13


def test_calculate_player_points_three_cards():
    """test if the method correctly counts the number of points scored by the player 
    when the player has more than 2 cards and in them player has an ace"""
    # given
    card = Card('spades', 'Ace')
    card2 = Card('hearts', 'Ace')
    card3 = Card('hearts', 'Ace')
    player = Player()

    # when
    player = Player()
    player.take_card(card)
    player.take_card(card2)
    player.take_card(card3)

    # then
    assert player.calculate_points() == 3
