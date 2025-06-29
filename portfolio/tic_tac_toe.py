import random

class TicTacToe:
    def __init__(self):

        self.grid={"1":"", "2":"", "3":"",
                   "4":"", "5":"", "6":"" ,
                   "7":"", "8":"", "9":""}
        self.winning_combos=[["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], #horizontl
                             ["1", "4", "7"], ["2", "5", "8"], ["3", "6", "9"], #verticl
                             ["1", "5", "9"], ["3", "5", "7"]] #diagonal
        self.combo = None
        self.message = None
        self.game_over = False
        self.position = None
        self.current_player = "Player 1"
        self.player_symbol = "X"


    def validate_position(self, position):
        """Validate if position is valid and available"""
        if position not in self.grid.keys():
            self.message = "This is outside the grid. Place your mark between 1 and 9!"
            return False
        elif self.grid[position] != "":
            self.message = f"This place is already taken {position}"
            return False
        else:
            return True

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
        elif self.grid["5"]== "":
            self.position = "5"
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

    def next_move(self, pos):
        """Main game loop - only handles input and orchestration"""
        while not self.game_over:
            if self.current_player == "Player 1":
                self.position = pos
            elif self.current_player == "Player 2":
                self.get_ai_move()

            if self.validate_position(self.position):
                self.make_move(self.position)
                if self.game_over:
                    print(self.message)
                    break
                else:
                    print(self.grid)

            else:
                print(self.message)


    def check_if_winner(self):

        result_player1 = [k for k,v in self.grid.items() if v=="X"]
        result_player2 = [k for k,v in self.grid.items() if v=="O"]

        for combo in self.winning_combos:
            if all(item in result_player1 for item in combo):
                self.message = "Player 1 wins!"
                self.game_over = True
                break
            elif all(item in result_player2 for item in combo):
                self.message = "Player 2 wins"
                self.game_over = True
                break
            else:
                self.game_over = False
                self.has_places_left()

if __name__ == "__main__":
    game = TicTacToe()
    game.next_move()

