"""
Matching Coin Game: Player
Gaven Huynh
This file defines the player class which represents the player.
Each player will have an attached name, "wallet" and coin object they can toss.
March 12, 2026
"""

from coin import Coin

class Player:
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__wallet: int = 20
        self.__coin: Coin = Coin()
    
    def toss_coin(self) -> str:
        self.__coin.toss()

    def get_coin_side(self) -> str:
        return self.__coin.get.side()