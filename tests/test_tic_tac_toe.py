from portfolio.tic_tac_toe import TicTacToe


class TestTicTacToe(object):

    def setup_method(self):
        '''Run before each test'''
        self.game = TicTacToe()

    def test_no_winner_empty_grid(self):
        """Test that no winner is declared on empty grid"""
        self.game.check_winner()
        assert self.game.winner is None
        assert self.game.game_over is False

    def test_horizontal_win_middle_row(self):
        """Test winning with middle horizontal row"""
        self.game.grid["A4"] = "X"
        self.game.grid["A5"] = "X"
        self.game.grid["A6"] = "X"

        self.game.check_winner()

        assert self.game.winner == "Player 1 wins!"
        assert self.game.game_over is True


    def text_game_draw(self):
        """Test grid has no winner but has no open places left"""
        self.grid = {"A1": "X", "A2": "X", "A3": "O",
                     "A4": "O", "A5": "O", "A6": "X",
                     "A7": "X", "A8": "X", "A9": "O"}

        self.game.check_winner()
        assert self.game.winner == "Player 1 wins!"
        assert self.game.game_over is True