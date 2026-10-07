from collections import Counter
def scrabble(letters, word):
    counter_word = Counter(word)
    counter_letters = Counter(letters)
    return counter_word <= counter_letters