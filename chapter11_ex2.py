def shift_word(word, shift):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = range(len(letters))
    letter_map = dict(zip(letters, numbers))

    result = []
    for letter in word:
        number = letter_map[letter]
        shifted = (number + shift) % 26
        result.append(letters[shifted])
    return "".join(result)
print(shift_word("cheer", 7))
    