"""Game mode"""
from deck import Deck
from player import Player
from exceptions import GameOverException, GameOverUserException, GameOverCroupierException


class Game:
    def __init__(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()

    @staticmethod
    def _print_menu():
        print('Co chcesz zrobić? ')
        print(' 0 - dobieram kartę')
        print(' 1 - pasuje')

    def _croupier_plays(self, user_points):
        """Croupier plays"""
        croupier = Player()
        while croupier.calculate_points() <= user_points:
            croupier.take_card(self.deck.hit())

        return croupier.calculate_points(), croupier.cards

    def _user_plays(self):
        """User plays"""
        user = Player()
        for _ in range(2):
            user.take_card(self.deck.hit())

        while True:
            print()
            print('Karty gracza:', user.cards)
            print('Twoja liczba punktów:', user.calculate_points())
            print()
            self._print_menu()
            choice = int(input('Wybierz 0 lub 1 -> '))
            if choice == 0:
                user.take_card(self.deck.hit())
                print()
                # print('Karty gracza:', user.cards)
                print('Twoja liczba punktów:', user.calculate_points())
                print()
            elif choice == 1:
                print()
                print('Karty gracza:', user.cards)
                print('Twoja liczba punktów:', user.calculate_points())
                print()
                return user.calculate_points()
            else:
                print('Dokonałeś złego wyboru')

    def play(self):
        """Play a game"""
        try:
            user_points = self._user_plays()
        except GameOverException as error:
            # lepsze ukazanie błedu, pokaże ze zaczął się już w playerze
            raise GameOverUserException from error
        try:
            croupier_points, croupier_cards = self._croupier_plays(user_points)
            print('Punkty krupiera:', croupier_points)
            print('Karty krupiera:', croupier_cards)
        except GameOverException as error:
            raise GameOverCroupierException from error

        #  jesli nikt nie przekroczy 21 pkt to wiadomo ze wygral krupier
        # bo on gra w nieskonczonosc az bedzie mial wiecej pkt niz gracz
        print('Koniec gry, wygrana krupiera')
