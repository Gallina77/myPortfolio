import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from portfolio.tic_tac_toe import TicTacToe

class TestTicTacToe:

    def setup_method(self):
        '''Run before each test'''
        self.game = TicTacToe()

    def test_outside_the_grid(self):
        result = self.game.validate_position('A10')
        assert not result
        assert self.game.message == "This is outside the grid. Place your mark between A1 and A9!"

    def test_position_taken(self):
        self.game.grid['A1'] = 'X'
        result = self.game.validate_position('A1')
        assert not result
        assert self.game.message == "This place is already taken A1"

    def test_draw_game(self):
        self.game.grid = {"A1":"X", "A2":"O", "A3":"X",
                          "A4":"", "A5":"O", "A6":"X" ,
                          "A7":"O", "A8":"X", "A9":"O"}

        self.game.make_move('A4')
        assert self.game.message == "It's a Draw!"
        assert self.game.game_over

    def test_valid_position(self):
        result = self.game.validate_position('A1')
        assert result

    def test_switch_player(self):
        self.game.make_move('A1')
        assert self.game.grid['A1'] == "X"
        self.game.make_move('A2')
        assert self.game.grid['A2'] == "O"

    def test_draw_game(self):
        self.game.grid = {"A1":"X", "A2":"O", "A3":"X",
                          "A4":"", "A5":"O", "A6":"X" ,
                          "A7":"O", "A8":"X", "A9":"O"}

        self.game.make_move('A4')
        assert self.game.message == "It's a Draw!"
        assert self.game.game_over

    def test_horizontal_strike(self):
        self.game.grid = {"A1":"X", "A2":"", "A3":"X",}
        self.game.make_move('A2')
        assert self.game.message == "Player 1 wins!"
        assert self.game.game_over

    def test_position(self):
        self.game.make_move('A2')
        self.game.grid = {"A1":"", "A2":"X", "A3":"",}
        self.game.make_move('A1')
        assert self.game.grid == {"A1":"O", "A2":"X", "A3":"",}
        assert not self.game.game_over

    def test_vertical_strike(self):
        self.game.grid = {"A1": "O", "A2": "X", "A3": "O",
                          "A4": "O", "A5": "O", "A6": "X",
                          "A7": "", "A8": "X", "A9": "X"}
        self.game.make_move('A7')
        assert self.game.message == "Player 1 wins!"
        assert self.game.game_over

    def test_diagonal_strike(self):
        self.game.grid = {"A1": "O", "A2": "O", "A3": "",
                          "A4": "O", "A5": "X", "A6": "X",
                          "A7": "X", "A8": "X", "A9": "X"}
        self.game.make_move('A3')
        assert self.game.message == "Player 1 wins!"
        assert self.game.game_over

    def test_ai_move_center(self):
        self.game.grid = {"A1": "X", "A2": "", "A3": "",
                          "A4": "X", "A5": "", "A6": "",
                          "A7": "O", "A8": "", "A9": ""}
        self.game.get_ai_move()
        assert self.game.has_two_marks("O") == False
        assert self.game.has_two_marks("X") == False
        assert self.game.position == "A5"

    def test_ai_winning(self):
        self.game.grid = {"A1":"X", "A2":"O", "A3":"X",
                          "A4":"", "A5":"X","A6":"O" ,
                          "A7":"O", "A8":"", "A9":"O"}
        self.game.get_ai_move()
        assert self.game.has_two_marks("O") == True
        assert self.game.combo == ["A7", "A8", "A9"]
        assert self.game.position == "A8"

    def test_ai_blocking_opponent(self):
        self.game.grid = {"A1":"", "A2":"", "A3":"",
                          "A4":"X", "A5":"X", "A6":"" ,
                          "A7":"", "A8":"", "A9":""}
        self.game.get_ai_move()
        assert self.game.has_two_marks("X") == True
        assert self.game.combo == ["A4", "A5", "A6"]
        assert self.game.position == "A6"