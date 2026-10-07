def uses_none(word, forbidden):
    new_set = set(word)
    return new_set.isdisjoint(forbidden)