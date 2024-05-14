from game_class import GameStrategy, GameMove

import random


class ImportedStrat(GameStrategy):
    def __init__(self) -> None:
        super().__init__(
            name="Nicer Bob", author="Nobu", description="too lazy to explain"
        )

    def next_play(
        self, player_history: list[GameMove], opponent_history: list[GameMove]
    ) -> GameMove:
        global random

        """
        :param player_history: List of your moves
        :param opponent_history: List of the opponent's moves
        :return: Your next move
        """

        share_weight = sum([i.value for i in opponent_history])
        steal_weight = len(opponent_history) - share_weight

        return random.choices(
            [GameMove.SHARE, GameMove.STEAL], weights=(share_weight + 1, steal_weight)
        )[0]


# This line is required!
userGame = ImportedStrat()
