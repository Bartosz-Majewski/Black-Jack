"""Main - start a game"""
from game import Game
from exceptions import GameOverUserException, GameOverCroupierException

try:
    game = Game()
    game.play()
except GameOverCroupierException:
    print('Wygrał gracz!!')
except GameOverUserException:
    print('Wygrał krupier!!')
