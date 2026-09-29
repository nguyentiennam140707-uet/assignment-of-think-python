def check_word(word, available, required):
    a = word.upper()
    if len(a) >= 4 and required in a:
        for letter in a:
            if letter in available:
                return True
    else:
        return False

print(check_word('color', 'ACDLORT', 'R'))
print(check_word('ratatat', 'ACDLORT', 'R'))
print(check_word('rat', 'ACDLORT', 'R'))