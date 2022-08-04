import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):

    def setUp(self):
        self.scores = []
        self.home_win = {"home_score":1, "away_score":0}
        self.away_win = {"home_score":0, "away_score":1}
        self.draw = {"home_score":1, "away_score":1}
        self.scores.append(self.home_win)
        self.scores.append(self.away_win)
        self.scores.append(self.draw)
        

    # Test we get the right result string for a final score dictionary representing -

        # Home win
    def test_home_win(self):
        result = get_result(self.home_win)
        self.assertEqual("Home win", result)
        # Away win
    def test_away_win(self):
        result = get_result(self.away_win)
        self.assertEqual("Away win", result)
        # Draw
    def test_Draw(self):
        result = get_result(self.draw)
        self.assertEqual("Draw", result)

    # Test we get right list of result strings for a list of final score dictionaries. 
    def test_list_scores(self):
        result = get_results(self.scores)
        self.assertEqual(['Home win', 'Away win', 'Draw'], result)
        


if __name__ == "__main__":
    unittest.main()
