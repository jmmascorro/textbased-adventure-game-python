import unittest
import text_adventure 

class TestMain(unittest.TestCase):

    def test_main(self):
        self.assertEqual(text_adventure.Player.__init__(self, name="", turns=5, inventory=[], is_bleeding=False), text_adventure.Player.__init__(self, name="", turns=5, inventory=[], is_bleeding=False), "Should be equal")

if __name__ == '__main__':
    unittest.main()




