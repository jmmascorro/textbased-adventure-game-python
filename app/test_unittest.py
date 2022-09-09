import unittest
import text_adventure 

class TestMain(unittest.TestCase):

    def test_player_class(self):
        self.assertEqual(text_adventure.Player.__init__(self), text_adventure.Player.__init__(self, name="", turns=5, inventory=[], is_bleeding=False), "Initializing player class should be equal")

    def test_player1(self):
        self.assertIsInstance(text_adventure.player1, text_adventure.Player, "player1 should be an instance of Player")

if __name__ == '__main__':
    unittest.main()




