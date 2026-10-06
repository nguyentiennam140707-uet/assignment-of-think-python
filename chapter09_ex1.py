def has_find(word1, word2):
    lst = []
    for c in word1:
        lst.append(c)
        sorted(lst)
        for char in word2:
            for i in range(len(lst)):
                if lst[i] == char:
                    lst.remove(char)
        if len(lst) == 0:
            return True
        return False

print(has_find("stop", "tops"))