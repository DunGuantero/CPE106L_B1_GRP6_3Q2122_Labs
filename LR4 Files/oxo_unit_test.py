import unittest
from oxo_logic import game

class test_game(unittest.TestCase):
    def test_game_new_game(self):
        t = game()
        self.assertEqual(list(" " * 9), t.newGame())

    def test_game_generate_move(self):
        t = game()
        self.assertIn(t._generateMove(t.newGame()), container=[0,1,2,3,4,5,6,7,8])
        self.assertEqual(t._generateMove("XXXXXXXXX"), -1)

    def test_game_is_winning_move(self):
        t = game()
        self.assertTrue(t._isWinningMove("XXX      "))
        self.assertTrue(t._isWinningMove("X  X  X  "))
        self.assertTrue(t._isWinningMove("X   X   X"))

    def test_game_user_move(self):
        t = game()
        game1 = "XX       "
        self.assertEqual(t.userMove(game1, 2), "X")
        #self.assertEqual(t.userMove("XX       ", 3), "")

    def test_game_computer_move(self):
        t = game()
        self.assertEqual(t.computerMove("XX       "), "")
        self.assertEqual(t.computerMove("XXXXXXXXX"), "D")
        self.assertEqual(t.computerMove("OOOOOOOO "), "O")



if __name__ == '__main__':
    unittest.main()