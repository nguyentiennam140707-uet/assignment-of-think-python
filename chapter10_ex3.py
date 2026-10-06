def find_repeats(counter):
    repeats = []
    for key in counter:
        if counter[key] > 1:
            repeats.append(key)
    return repeats 