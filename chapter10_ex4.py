def value_counts(word):
    counter = {}

    for c in word:
        counter[c] = counter.get(c, 0) + 1
    return counter
def add_total(counter1, counter2):
    total = {}

    for key in counter1:
        total[key] = counter1[key]
    for key in counter2:
        total[key] = total.get(key, 0) + counter2[key]

    return total
counter1 = value_counts('brontosaurus')
counter2 = value_counts('apatosaurus')
print(add_total(counter1, counter2))