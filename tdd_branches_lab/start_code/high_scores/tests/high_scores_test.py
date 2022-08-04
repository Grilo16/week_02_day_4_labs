import unittest

from src.high_scores import latest, personal_best, personal_top_three, ordered_scores

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    def setUp(self):
        self.scores = [420, 42, 3, 69]
        self.scores_with_tie = [420, 42, 3, 69, 420]
        self.scores_less_than3 = [420, 69]
        self.scores_only_1 = [420]
    
    # Tests

    # Test latest score (the last thing in the list)
    def test_latest(self):
        self.assertEqual(69, latest(self.scores))

    # Test personal best (the highest score in the list)
    def test_best(self):
        self.assertEqual(420, personal_best(self.scores))

    # Test top three from list of scores
    def test_best_three(self):
        self.assertEqual([420, 69, 42], personal_top_three(self.scores))

    # Test ordered from highest tp lowest
    def test_ordered_scores(self):
        self.assertEqual([420, 69, 42, 3], ordered_scores(self.scores))

    # Test top three when there is a tie
    def test_best_three_with_tie(self):
        self.assertEqual([420, 420, 69], personal_top_three(self.scores_with_tie))

    # Test top three when there are less than three
    def test_best_three_less_then_three(self):
        self.assertEqual([420, 69], personal_top_three(self.scores_less_than3))

    # Test top three when there is only one
    def test_best_three_only_one(self):
        self.assertEqual([420], personal_top_three(self.scores_only_1))
    
