window = []
trigrams = {}

def count_trigram(trigram):
    trigrams[trigram] = trigrams.get(trigram, 0) + 1

def add_trigram(window):
    trigram = tuple(window)
    count_trigram(trigram)

def process_word_trigram(word):
    window.append(word)
    if len(window) == 3:
        add_trigram(window)
        window.pop(0)