def is_metathesis(word1, word2):
    if sorted(word1) != sorted(word2):
        return False
    
    distance = 0

    for a, b in zip(word1, word2):
        if a != b:
            distance += 1
    return distance == 2

def find_metathesis(words):
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word1 = words[i]
            word2 = words[j]
            if is_metathesis(word1, word2):
                print(word1, word2)
find_metathesis(["converse", "conserve", "abc"])