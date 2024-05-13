from game_class import GameMove

class Frued(GameStrategy):
    def __init__(self) -> None:
        # This is where your metadata will go:
        super().__init__(name="Frued", author="Kyle B.", description="END T4T!!")

    def next_play(self, player_history: list[GameMove], opponent_history: list[GameMove]) -> GameMove:
        """
        :param player_history: List of your moves
        :param opponent_history: List of the opponent's moves
        :return: Your next move
        """
        # This is where your strategy logic goes
        # Each item in the history arrays will be equal to GameMove.STEAL or GameMove.SHARE

        pHist = player_history
        oHist = opponent_history

        roundsPlayed = len(pHist)

        if roundsPlayed < 18:
            #complicated testing bits
            if [1,5,6,10,11,12].index(roundsPlayed) >= 0:
                return GameMove.STEAL
            else:
                return GameMove.SPLIT
        else:
            #identify is t4t
            if (oHist.index(GameMove.STEAL) == 2):
                return oHist[-1] #play t4t
            elif (oHist.index(GameMove.STEAL) == 7):
                if pHist[-1] == GameMove.SPLIT:
                    return GameMove.STEAL
                else:
                    return GameMove.SPLIT
            elif (oHist.index(GameMove.STEAL) == 13):
                if pHist[-1] == GameMove.STEAL and pHist[-2] == GameMove.STEAL:
                    return GameMove.SPLIT
                else:
                    return GameMove.STEAL
            elif sum(isinstance(x, GameMove.STEAL) for x in oHist[18:]) > (.5 * roundsPlayed-18):
                return GameMove.STEAL
            else:
                #t4t
                return oHist[-1]




# This line is required!
userGame = Freud()


