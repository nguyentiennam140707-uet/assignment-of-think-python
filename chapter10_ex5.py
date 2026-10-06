def is_interlocking(word):
    first = word[0::2]
    second = word[1::2]

    return first, second

print(is_interlocking("schooled"))