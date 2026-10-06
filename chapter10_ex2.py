def counter_value(word):
    counter = {}

    for letter in word:
        counter[letter] = counter.get(letter, 0) + 1
    return counter
    
def has_duplicates(word):
    counter = counter_value(word)
    for c in word:            
        if counter.get(c, 0) >= 2:
            return True
    return False

print(has_duplicates("hello"))