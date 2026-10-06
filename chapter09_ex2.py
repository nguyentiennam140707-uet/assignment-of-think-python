def is_palindrome(word):
    if list(reversed(word)) == list(word):
        return True
    return False
print(is_palindrome("rotator"))