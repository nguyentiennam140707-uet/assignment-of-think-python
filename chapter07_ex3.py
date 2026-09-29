def uses_all(word, required):
    for i in required:
        if i not in word:
            return False
    return True

print(uses_all('banana', 'ban'))
print(uses_all('apple', 'api'))
print(uses_all('cartload', 'ACDLORT'))