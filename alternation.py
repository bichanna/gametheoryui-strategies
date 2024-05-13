"""
Alternates between stealing and sharing.
by: Ari Stehney
"""
from game_class import GameStrategy, GameMove

class ImportedStrat(GameStrategy):
    def __init__(self) -> None:
        # This is where your metadata will go:
        super().__init__(name="Alternate", author="Ari S.", description="Alternates between stealing and sharing.")

    def next_play(self, player_history: list[GameMove], opponent_history: list[GameMove]) -> GameMove:
        """
        :param player_history: List of your moves
        :param opponent_history: List of the opponent's moves
        :return: Your next move
        """

        if len(player_history) == 0:
            return GameMove.STEAL

        return GameMove.STEAL if player_history[-1] == GameMove.SHARE else GameMove.SHARE

# This line is required!
userGame = ImportedStrat()
