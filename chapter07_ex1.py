def uses_none(word, forbidden):
    for i in forbidden:
        if i in word:
            return False
    return True

print(uses_none('banana', 'abc'))