class Solution:
    # If Alice starts the game with an even number, she will automatically win the game.
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0
