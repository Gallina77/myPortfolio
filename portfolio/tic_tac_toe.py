import random

class TicTacToe:
    def __init__(self):

        self.grid={"0":"", "1":"", "2":"",
                   "3":"", "4":"", "5":"" ,
                   "6":"", "7":"", "8":""}
        self.winning_combos=[["0", "1", "2"], ["3", "4", "5"], ["6", "7", "8"], #horizontl
                             ["0", "3", "6"], ["1", "4", "7"], ["2", "5", "8"], #verticl
                             ["0", "4", "8"], ["2", "4", "6"]] #diagonal

        self.combo = None
        self.message = "Let's play TicTacToe!"
        self.game_over = False
        self.position = None
        self.current_player = None
        self.player_symbol = None


    def has_places_left(self):
        left = ([v for v in self.grid.values() if v == ""])
        if len(left) > 0:
            self.game_over = False
        else:
            self.message = "It's a Draw!"
            self.game_over = True

    def has_two_marks(self, mark):
        for combo in self.winning_combos:
            count = sum(1 for pos in combo if self.grid[pos] == mark)
            if count==2 and any(self.grid[pos] == "" for pos in combo):
                self.combo = combo
                return True
        return False

    def get_ai_move(self):
        '''Player 2 tactics to identify the best move'''
        # checks if Player 2 needs to block opponent from winning o
        if self.has_two_marks("X"):
            for pos in self.combo:
                if self.grid[pos] == "":
                    self.position = pos
        # checks winning combo only missing one position in that row
        elif self.has_two_marks("O"):
            for pos in self.combo:
                if self.grid[pos] == "":
                    self.position = pos
        # takes center if available
        elif self.grid["4"]== "":
            self.position = "4"
        # takes any other available place
        else:
            left_places = [k for k, v in self.grid.items() if v == ""]
            self.position = random.choice(left_places)

    def switch_player(self):
        if self.current_player == "Player 1":
            self.current_player = "Player 2"
            self.player_symbol = "O"
        else:
            self.current_player = "Player 1"
            self.player_symbol = "X"

    def make_move(self, position):
        """Make a move at the given position"""
        self.grid[position] = self.player_symbol
        self.check_if_winner()
        if not self.game_over:
            self.switch_player()
            self.message = f"It's your turn {self.current_player}"

    def player_move(self, pos):
        self.current_player = "Player 1"
        self.player_symbol = "X"
        self.make_move(pos)

    def ai_move(self):
        self.current_player = "Player 2"
        self.player_symbol = "O"
        self.get_ai_move()
        self.make_move(self.position)

    def check_if_winner(self):
        result_current_player = [k for k,v in self.grid.items() if v==self.player_symbol]
        for combo in self.winning_combos:
            if all(item in result_current_player for item in combo):
                self.message = f"{self.current_player} wins!"
                self.game_over = True
                break
            else:
                self.game_over = False
                self.has_places_left()



