def value_count(word):
    counter = {}

    for letter in word:
        counter[letter] = counter.get(letter, 0) + 1
    return counter

print(value_count('brontosaurus'))