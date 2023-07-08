def is_anagram(first_string: str, second_string: str):
    first_string = first_string.lower()
    second_string = second_string.lower()

    if len(first_string) != len(second_string):
        return False
    if first_string == "" or second_string == "":
        return False

    return ("", "", True)
