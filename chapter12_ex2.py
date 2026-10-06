successor_map = {}
window = []

def add_trigram(trigram):
    first = trigram[0]
    second = trigram[1]
    third = trigram[2]

    key = (first, second)

    if key not in successor_map:
        successor_map[key] = []

    successor_map[key].append(third)


def process_word_trigram(word):
    window.append(word)

    if len(window) == 3:
        add_trigram(window)
        window.pop(0)