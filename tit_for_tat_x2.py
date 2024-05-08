"""
Template game theory strategy for GameTheoryUI.
by: Owais Oumera
"""
from game_class import GameStrategy, GameMove

import random

class ImportedStrat(GameStrategy):
    def __init__(self) -> None:
        # This is where your metadata will go:
        super().__init__(name="Tit for tat x2", author="Owais O.", description="If you recive two steals in a row, steal. Otherwise, share.")

    def next_play(self, player_history: list[GameMove], opponent_history: list[GameMove]) -> GameMove:
        """
        :param player_history: List of your moves
        :param opponent_history: List of the opponent's moves
        :return: Your next move
        """
        if len(opponent_history) < 2:
            return GameMove.SHARE
        elif (opponent_history[-1] == GameMove.STEAL and opponent_history[-2] == GameMove.STEAL) or random.randint(0, 10) == 0:
            return GameMove.STEAL
        else:
            return GameMove.SHARE

# This line is required!
userGame = ImportedStrat()