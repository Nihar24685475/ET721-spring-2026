# Improved Connect 4 Game

class Connect4:
    ROWS = 6
    COLS = 7

    def __init__(self):
        self.board = [[' ' for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.current_player = 'X'

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def print_board(self):
        print("\nCurrent Board:")
        for row in self.board:
            print('|', end='')
            for cell in row:
                if cell == 'X':
                    print('\033[91mX\033[0m', end='|')  # Red for X
                elif cell == 'O':
                    print('\033[94mO\033[0m', end='|')  # Blue for O
                else:
                    print(' ', end='|')
            print()
        print('---------------')
        print(' 1 2 3 4 5 6 7')

    def drop_chip(self, column):
        """Drop a chip in the chosen column (1-7)."""
        if not (1 <= column <= self.COLS):
            return False

        for row in range(self.ROWS - 1, -1, -1):
            if self.board[row][column - 1] == ' ':
                self.board[row][column - 1] = self.current_player
                return True
        return False  # Column full

    def check_win(self, player):
        """Check if a player has 4 in a row (horizontal, vertical, diagonal)."""
        # Horizontal check
        for row in range(self.ROWS):
            for col in range(self.COLS - 3):
                if all(self.board[row][col + i] == player for i in range(4)):
                    return True

        # Vertical check
        for row in range(self.ROWS - 3):
            for col in range(self.COLS):
                if all(self.board[row + i][col] == player for i in range(4)):
                    return True

        # Diagonal (down-right)
        for row in range(self.ROWS - 3):
            for col in range(self.COLS - 3):
                if all(self.board[row + i][col + i] == player for i in range(4)):
                    return True

        # Diagonal (up-right)
        for row in range(3, self.ROWS):
            for col in range(self.COLS - 3):
                if all(self.board[row - i][col + i] == player for i in range(4)):
                    return True

        return False

    def is_full(self):
        """Check if the board is full."""
        return all(self.board[0][col] != ' ' for col in range(self.COLS))

    def play_game(self):
        """Main game loop."""
        print("Welcome to Connect 4!\n")
        while True:
            self.print_board()
            print(f"Player {self.current_player}'s turn.")

            try:
                column = int(input("Enter column (1-7): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 7.")
                continue

            if not self.drop_chip(column):
                print("Invalid move! Column is full or out of range. Try again.")
                continue

            if self.check_win(self.current_player):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break

            if self.is_full():
                self.print_board()
                print("It's a tie! No more moves left.")
                break

            self.switch_player()


if __name__ == "__main__":
    Connect4().play_game()
