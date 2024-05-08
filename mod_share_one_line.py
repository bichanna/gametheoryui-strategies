"""
Template game theory strategy for GameTheoryUI.
By: Owais
Idea: Nobu
"""
from game_class import GameStrategy, GameMove

import random
class ImportedStrat(GameStrategy):
    def __init__(self) -> None:
        # This is where your metadata will go:
        super().__init__(name="Mod Share 1line", author="Owais", description="Mod Share... you get it mod -> % -> percent!!!")

    def next_play(self, player_history: list[GameMove], opponent_history: list[GameMove]) -> GameMove:
        global random
        """
        :param player_history: List of your moves
        :param opponent_history: List of the opponent's moves
        :return: Your next move
        """
        return eval("GameMove."+["STEAL","SHARE"][random.choices([0,1], weights = [1-sum(opponent_history)/len(opponent_history),sum(opponent_history)/len(opponent_history)])])

# This line is required!
userGame = ImportedStrat()