"""
Template game theory strategy for GameTheoryUI.
by: June Valone
Coder: Owais Oumera
"""
from game_class import GameStrategy, GameMove

import random

class ImportedStrat(GameStrategy):
    def __init__(self) -> None:
        # This is where your metadata will go:
        super().__init__(name="Passive aggressive", author="June V.", description="Initiates retaliation five rounds in. Retaliates twice no matter what after the first player retaliates. But after two, goes back to agreeing until the other retaliates again.")

    def next_play(self, player_history: list[GameMove], opponent_history: list[GameMove]) -> GameMove:
        """
        :param player_history: List of your moves
        :param opponent_history: List of the opponent's moves
        :return: Your next move
        """
        if len(opponent_history) < 6:
            return GameMove.SHARE
        elif opponent_history[-1] == GameMove.STEAL or opponent_history[-2] == GameMove.STEAL:
            return GameMove.STEAL
        else:
            return GameMove.SHARE

# This line is required!
userGame = ImportedStrat()