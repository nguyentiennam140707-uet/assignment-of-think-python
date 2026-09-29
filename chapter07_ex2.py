def uses_only(word, available):
    for i in word:
        if i not in available:
            return False
    return True

print(uses_only('banana', 'ban'))
print(uses_only('apple', 'apl'))