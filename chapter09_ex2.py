def is_anagram(word):
    word = list(word)
    if word[0:] == word[::-1]:
        return True
    else: 
        return False

print(is_anagram('cbababc'))