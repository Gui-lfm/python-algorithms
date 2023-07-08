def is_palindrome_recursive(word: str, low_index: int, high_index: int):
    if word == "":
        return False

    if low_index >= high_index:
        return True

    if word[low_index] == word[high_index]:
        low_index = low_index + 1
        high_index = high_index - 1
        return is_palindrome_recursive(word, low_index, high_index)

    return False
