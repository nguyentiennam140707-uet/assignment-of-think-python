def value_counters(word):
    counter = {}
    for c in word:
        counter[c] = counter.get(c, 0) + 1
    return counter

def most_frequent_letters(word):
    counter = value_counters(word)
    letters = sorted(counter, key = counter.get, reverse = True)
    return letters

print(most_frequent_letters("abcabcbaaanv"))
