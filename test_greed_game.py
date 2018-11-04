# -*- coding: utf-8 -*-

import unittest

from greed_game import GreedGame


class PlayerMock(object):
    def __init__(self, points):
        self._points = points

    @property
    def points(self):
        return self._points


class GreedGameTest(unittest.TestCase):
    def test_get_winner_after_final_round(self):
        game = GreedGame()
        p1 = PlayerMock(1000)
        p2 = PlayerMock(3000)
        game.add_player(p1)
        game.add_player(p2)
        game.one_round()
        self.assertTrue(game.final_round)
        game.one_round()
        self.assertEqual(p2, game.get_winner())

    def test_get_winner_before_final_round(self):
        game = GreedGame()
        p1 = PlayerMock(100)
        p2 = PlayerMock(200)
        game.add_player(p1)
        game.add_player(p2)
        game.one_round()
        self.assertFalse(game.final_round)
        game.one_round()
        with self.assertRaises(ValueError):
            game.get_winner()


if __name__ == "__main__":
    unittest.main()
