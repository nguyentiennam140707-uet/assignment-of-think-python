def uses_only(word, available):
    for i in word:
        if i not in available:
            return False
    return True

def uses_all( word, required):
    return uses_only(required, word)