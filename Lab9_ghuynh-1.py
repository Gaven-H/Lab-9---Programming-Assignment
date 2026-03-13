"""
Matching Coin Game
Gaven Huynh
This program will run the Match Coins game where two players will toss a coin.
They will then gain or lose points based on the resulting toss.
Match 12, 2026
"""

from player import Player

def main() -> None:
    player1: Player = Player("Player 1")
    player2: Player = Player("Player 2")

    print("--- Cain Match Game ---")
    print(f"{player1.get_name()} has {player1.get_wallet()} coins!")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins!")

    play: str = input("Do you want to toss the coins? (y/n): ")

    while play.lower() == "y":
        print("Tossing. . .")

        player1.toss_coin()
        player2.toss_coin()

        side1: str = player1.get_coin_side()
        side2: str = player2.get_coin_side()
        
        print(f"{player1.get_name()} has tossed {side1}")
        print(f"{player2.get_name()} has tossed {side2}")

        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print(". . . It's a Match! Player 1 wins a coin from Player 2.")
        else:
            player2.win_coin()
            player1.lose_coin()
            print(". . . No Match! Player 2 wins a coin from Player 1.")