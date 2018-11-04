# -*- coding: utf-8 -*-


class GreedGame(object):
    def __init__(self):
        self._players = []
        self._final_round = False
        self._is_end = False

    def add_player(self, player):
        self._players.append(player)

    @property
    def final_round(self):
        return self._final_round

    def one_round(self):
       if self._final_round:
            self._is_end = True
            return
       for p in self._players:
            if p.points >= 3000:
                self._final_round = True
                break

    def get_winner(self):
        if not self._is_end:
            raise ValueError
        winner = self._players[0]
        for p in self._players[1:]:
            if p.points > winner.points:
                winner = p
        return winner
