from games import *

class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a list with number of objects in each row."""

    def __init__(self, board=[3,1]):
        self.board = board
        moves = [(x, y) for x in range(0, len(board))
                 for y in range(1, board[x] + 1)]
        self.initial = GameState(to_move='MAX', utility=0, board=self.board, moves=moves)
        # raise NotImplementedError

    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves

    def result(self, state, move):
        board = state.board.copy()
        board[move[0]] = board[move[0]] - move[1]
        newMoves = list([(x, y) for x in range(0, len(board))
                     for y in range(1, board[x] + 1)])
        return GameState(to_move=('MIN' if state.to_move == 'MAX' else 'MAX'),
                         utility=0,
                         board=board,
                         moves=newMoves)
        # raise NotImplementedError

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        return state.utility if player == 'MAX' else -state.utility
        # raise NotImplementedError

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        return state.utility != 0 or len(state.moves) == 0
        # raise NotImplementedError

    def display(self, state):
        board = state.board
        print("board: ", board)

    def to_move(self, state):
        """Return the player whose move it is in this state."""
        return state.to_move

    def play_game(self, *players):
        """Play an n-person, move-alternating game."""
        state = self.initial
        self.display(state)
        while True:
            for player in players:
                move = player(self, state)
                if player == alpha_beta_player:
                    print(move)
                state = self.result(state, move)
                self.display(state)
                if self.terminal_test(state):
                    self.display(state)
                    return self.utility(state, self.to_move(self.initial))

if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1]) # Creating the game instance
    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    # print(nim.initial.board) # must be [0, 5, 3, 1]
    # print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    # print(nim.result(nim.initial, (1,3)))
    # nim.display(nim.result(nim.initial, (1,3)))
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first 
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")

