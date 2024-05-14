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

        if len(opponent_history) > 0:
            return [GameMove.STEAL, GameMove.SHARE][random.choices([0,1], weights = [1-sum([x.value for x in opponent_history])/len(opponent_history),sum([x.value for x in opponent_history])/len(opponent_history)], k=1)[0]]
        else:
            return GameMove.SHARE

# This line is required!
userGame = ImportedStrat()
