"""
Matching Coin Game: Coin
Gaven Huynh
This program will define the Coin class which simulates a single coin being tossed.
It can land on heads or tails.
March 12, 2026
"""
import random

class Coin:
    def __init__(self) -> None:
        self.__sideup: str = random.choice(["Heads", "Tails"])

    def toss(self) -> None:
        result: int = random.randint(0,1)
        
        if result == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"