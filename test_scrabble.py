import unittest
import scrabble_calc


class TestScrabble(unittest.TestCase):

    TEST_LIST_OF_WORDS = ["adbfkjq", "zzzzzzzzzz", "", "lalala", "abrakadabra", "qqqqqqqqqq"]

    TEST_DICTIONARY = {"adbfkjq": 33,
                       "zzzzzzzzzz": 100,
                       "": 0,
                       "lalala": 6,
                       "abrakadabra": 20,
                       "qqqqqqqqqq": 100}

    def test_count_scores_for_words_in_dictionary(self):
        scrabble_calculator = scrabble_calc.ScrabbleCalc(self.TEST_LIST_OF_WORDS)
        self.assertEqual(scrabble_calculator.words_scores_dictionary, self.TEST_DICTIONARY)

    def test_count_word_score(self):
        scrabble_calculator = scrabble_calc.ScrabbleCalc()
        self.assertEqual(scrabble_calculator.count_word_score("scrabble"), 14)
        self.assertEqual(scrabble_calculator.count_word_score("marta"), 7)
        self.assertEqual(scrabble_calculator.count_word_score("quickly"), 25)
        self.assertEqual(scrabble_calculator.count_word_score(""), 0)
        self.assertEqual(scrabble_calculator.count_word_score("qqqqq"), 50)

    def test_choose_the_highest_score(self):
        scrabble_calculator = scrabble_calc.ScrabbleCalc(self.TEST_LIST_OF_WORDS)
        self.assertEqual(scrabble_calculator.choose_the_highest_score(), 100)

    def test_find_word_with_score(self):
        scrabble_calculator = scrabble_calc.ScrabbleCalc(self.TEST_LIST_OF_WORDS)
        self.assertEqual(scrabble_calculator.find_word_with_score(0), "")
        self.assertEqual(scrabble_calculator.find_word_with_score(1), None)
        self.assertIn(scrabble_calculator.find_word_with_score(100), ["zzzzzzzzzz", "qqqqqqqqqq"])
        self.assertEqual(scrabble_calculator.find_word_with_score(33), "adbfkjq")


if __name__ == '__main__':
    unittest.main()
