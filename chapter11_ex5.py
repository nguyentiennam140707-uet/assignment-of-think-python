def word_distance(word1, word2):
    distance = 0

    for a, b in zip(word1, word2):
        if a != b:
            distance += 1
    return distance
print(word_distance("hello", "jello"))