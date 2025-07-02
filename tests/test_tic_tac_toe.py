import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from portfolio.tic_tac_toe import TicTacToe

class TestTicTacToe:

    def setup_method(self):
        '''Run before each test'''
        self.game = TicTacToe()


    def test_draw_game(self):
        self.game.grid = {"0":"X", "1":"O", "2":"X",
                          "3":"", "4":"O", "5":"X" ,
                          "6":"O", "7":"X", "8":"O"}

        self.game.player_move('3')
        assert self.game.message == "It's a Draw!"
        assert self.game.game_over

    def test_horizontal_strike(self):
        self.game.grid = {"0": "X", "1": "", "2": "X",
                          "3": "", "4": "", "5": "X",
                          "6": "", "7": "X", "8": "O"}
        self.game.player_move('1')
        assert self.game.message == "Player 1 wins!"
        assert self.game.game_over

    def test_vertical_strike(self):
        self.game.grid = {"0":"X", "1":"O", "2":"X",
                          "3":"X", "4":"O", "5":"X" ,
                          "6":"", "7":"X", "8":"O"}

        self.game.player_move('6')
        assert self.game.message == "Player 1 wins!"
        assert self.game.game_over

    def test_diagonal_strike(self):
        self.game.grid = {"0":"X", "1":"O", "2":"",
                          "3":"X", "4":"X", "5":"O" ,
                          "6":"O", "7":"X", "8":""}

        self.game.player_move('8')
        assert self.game.message == "Player 1 wins!"
        assert self.game.game_over

    def test_ai_move_center(self):
        self.game.grid = {"0":"X", "1":"", "2":"",
                          "3":"", "4":"", "5":"" ,
                          "6":"", "7":"", "8":""}
        self.game.get_ai_move()
        assert self.game.has_two_marks("O") == False
        assert self.game.has_two_marks("X") == False
        assert self.game.position == "4"

    def test_ai_winning(self):
        self.game.grid = {"0":"X", "1":"", "2":"X",
                          "3":"X", "4":"O", "5":"" ,
                          "6":"O", "7":"O", "8":""}
        self.game.get_ai_move()
        assert self.game.has_two_marks("O") == True
        assert self.game.position == "1"


    def test_ai_blocking_opponent(self):
        self.game.grid = {"0":"O", "1":"X", "2":"X",
                          "3":"X", "4":"", "5":"" ,
                          "6":"O", "7":"X", "8":""}
        self.game.get_ai_move()
        assert self.game.has_two_marks("X") == True
        assert self.game.combo == ["1", "4", "7"]
        assert self.game.position == "4"