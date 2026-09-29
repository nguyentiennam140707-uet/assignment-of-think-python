def check_word(word, target_word):
    correct_words = 0
    for i in range(len(target_word)):
        for j in range(len(word)):
            if target_word[i] == word[j]:
                correct_words += 1
                if i == j:
                    print("Yes, " + target_word[i] + " is in the word and in the correct position")
                else: print("Yes, have " + target_word[i] + " in target_word")
    for letter in word:
        if letter not in target_word:
            print("Dont have " + letter + " in target_word")
    remaining_words = len(target_word) - correct_words
    print("Remaining words left: " + str(remaining_words))
check_word('cpeak', 'spade')
