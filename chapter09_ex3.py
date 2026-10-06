def reverse_sentence(word):
    lst = word.split()
    lst.reverse()

    lst[0] = lst[0].capitalize()
    for i in range(1, len(lst)):
        lst[i] = lst[i].lower()

    return " ".join(lst)

print(reverse_sentence("Reverse this sentence"))