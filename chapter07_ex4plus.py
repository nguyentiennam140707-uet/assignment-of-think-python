def check_word(word, available, required):
    a = word.upper()
    if len(a) >= 4 and required in a:
        for letter in a:
            if letter in available:
                return True
    else:
        return False
def uses_all(word, required):
    for i in required:
        if i not in word:
            return False
    return True

def word_score(word, available):
    totalPoints = 0
    word = word.upper()
    if uses_all(word, available) == True:
        totalPoints += 7
    if len(word) == 4:
        totalPoints += 1
    elif len(word) >= 5:
        totalPoints += len(word)
    else: 
        return 0
    print(totalPoints)

word_score('card', 'ACDLORT')
word_score('color', 'ACDLORT')
word_score('cartload', 'ACDLORT')