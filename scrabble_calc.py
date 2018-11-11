import random


class ScrabbleCalc:
    SCRABBLES_SCORES = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                        (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
    LETTER_SCORES = {letter: score for score, letters in SCRABBLES_SCORES
                     for letter in letters.split()}

    def __init__(self, list_of_words=None):
        if list_of_words is None:
            self.list_of_words = []
        else:
            self.list_of_words = list_of_words
        self.words_scores_dictionary = self.count_scores_for_words_in_dictionary()

    def count_word_score(self, word):
        score = 0
        for letter in word.upper():
            score = score + self.LETTER_SCORES[letter]
        return score

    def count_scores_for_words_in_dictionary(self):
        scores = {}
        for word in self.list_of_words:
            score = self.count_word_score(word)
            scores[word] = score
        return scores

    def choose_the_highest_score(self):
        word_with_max_score = max(zip(self.words_scores_dictionary.values(), self.words_scores_dictionary.keys()))
        return word_with_max_score[0]

    def find_word_with_score(self, search_score):
        words = []
        for word, score in self.words_scores_dictionary.items():
            if score == search_score:
                words.append(word)
        if len(words) > 0:
            return random.choice(words)
