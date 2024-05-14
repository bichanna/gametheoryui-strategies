"""
Probability informed strategy, uses track record.
by: Ari Stehney
"""
from game_class import GameStrategy, GameMove

import random
import collections

class ImportedStrat(GameStrategy):
    def __init__(self) -> None:
        # This is where your metadata will go:
        super().__init__(name="Probability Informed x5", author="Ari S.", description="Random chance weighted by past 5 rounds.")

    def next_play(self, player_history: list[GameMove], opponent_history: list[GameMove]) -> GameMove:
        global random, collections
        """
        :param player_history: List of your moves
        :param opponent_history: List of the opponent's moves
        :return: Your next move
        """

        cntr = collections.Counter(opponent_history[-6: -1])
        opp_list = {"GameMove.SHARE": 1, "GameMove.STEAL": 1}

        for i in cntr.elements():
            opp_list[str(i)] = cntr[i]

        print(opp_list)

        return random.choices(
            [GameMove.SHARE, GameMove.STEAL],
            weights=(opp_list["GameMove.SHARE"], opp_list["GameMove.STEAL"]),
            k=1
        )[0]

# This line is required!
userGame = ImportedStrat()
