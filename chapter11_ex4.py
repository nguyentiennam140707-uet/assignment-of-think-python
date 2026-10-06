def find_anagrams(words):
    anagrams = {}

    for word in words:
        key = ''.join(sorted(word))

        if key not in anagrams:
            anagrams[key] = []

        anagrams[key].append(word)

    for group in anagrams.values():
        if len(group) > 1:
            print(group)