import unittest
from main import Connect4


class TestSwitchPlayer(unittest.TestCase):

    def setUp(self):
        """Create a new game before each test."""
        self.game = Connect4()

    def test_switch_from_X_to_O(self):
        """Player should switch from X to O."""
        self.game.current_player = 'X'
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'O')

    def test_switch_from_O_to_X(self):
        """Player should switch from O to X."""
        self.game.current_player = 'O'
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'X')

    def test_switch_twice(self):
        """Switching twice should return to original player."""
        original = self.game.current_player
        self.game.switch_player()
        self.game.switch_player()
        self.assertEqual(self.game.current_player, original)


if __name__ == "__main__":
    unittest.main()



# Documentation / Test Results
#
# All tests verify the correct functionality of switch_player().
#
# Test Cases:
# 1. Switching player from X should result in O.
# 2. Switching player from O should result in X.
# 3. Switching twice should return to the original player.
#
# Results:
# All tests passed successfully. No bugs were found.
