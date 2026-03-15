import pytest
from main import Connect4


def test_successful_chip_drop():
    """Chip should drop successfully into empty column."""
    game = Connect4()
    result = game.drop_chip(1)
    assert result == True
    assert game.board[5][0] == 'X'


def test_column_full():
    """Dropping chip into full column should return False."""
    game = Connect4()

    for _ in range(game.ROWS):
        game.drop_chip(1)

    result = game.drop_chip(1)
    assert result == False


def test_invalid_column_low():
    """Column less than 1 should return False."""
    game = Connect4()
    result = game.drop_chip(0)
    assert result == False


def test_invalid_column_high():
    """Column greater than 7 should return False."""
    game = Connect4()
    result = game.drop_chip(8)
    assert result == False


def test_full_board():
    """Test behavior when the board is full."""
    game = Connect4()

    for col in range(1, 8):
        for _ in range(game.ROWS):
            game.drop_chip(col)

    assert game.is_full() == True


# Documentation / Test Results
#
# Test Cases:
# 1. Successful chip drop into empty column.
# 2. Attempting to drop chip into a full column.
# 3. Attempting to drop chip into invalid column too low.
# 4. Attempting to drop chip into invalid column too high.
# 5. Checking board behavior when completely full.
#
# Results:
# All tests passed successfully.
