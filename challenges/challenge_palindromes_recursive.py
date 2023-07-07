def is_palindrome_recursive(word, low_index, high_index):
    if word is None:
        return False

    if len(word) <= 1:
        return True

    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(
            word[1:-1], low_index + 1, high_index - 1
        )

    return False


print(is_palindrome_recursive("", 0, 2))
