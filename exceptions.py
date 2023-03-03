"""Exceptions"""


class GameOverException(Exception):
    pass


class GameOverUserException(Exception):
    pass


class GameOverCroupierException(Exception):
    pass


class InvalidColor(Exception):
    """Exception when color in invalid"""


class InvalidValue(Exception):
    """Exception when value in invalid"""
