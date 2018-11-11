import argparse
import sys
import scrabble_calc

def read_words_from_file(filename):
    words = []
    with open(filename) as fp:
        lines = fp.read().splitlines()
        for word in lines:
            words.append(word.strip("\n"))
    return words


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Calculate scores for Scrabble Game',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    subparsers = parser.add_subparsers(dest="action", help='functions to execute')

    # python scrabble.py score "word"
    score_parser = subparsers.add_parser('score', help='count the score of the given word')
    score_parser.add_argument('word', type=str, help='word to calculate score')

    # python scrabble.py find 6 dictionary.txt
    find_parser = subparsers.add_parser('find', help='find word with given score')
    find_parser.add_argument('score', type=int, help='score to find a word from the dictionary')
    find_parser.add_argument('dictionary', type=str, help='dictionary file name')

    # python scrabble.py highest dictionary.txt
    highest_parser = subparsers.add_parser('highest', help='get the highest score from the dictionary')
    highest_parser.add_argument('dictionary', type=str, help='dictionary file name')

    args = parser.parse_args()

    if len(sys.argv) <= 1:
        parser.print_help()

    if args.action == "score":
        scrabble_calc = scrabble_calc.ScrabbleCalc()
        print(scrabble_calc.count_word_score(args.word))
    elif args.action == "highest":
        dictionary_words = read_words_from_file(args.dictionary)
        scrabble_calc = scrabble_calc.ScrabbleCalc(dictionary_words)
        print(scrabble_calc.choose_the_highest_score())
    elif args.action == "find":
        dictionary_words = read_words_from_file(args.dictionary)
        scrabble_calc = scrabble_calc.ScrabbleCalc(dictionary_words)
        print(scrabble_calc.find_word_with_score(args.score))
