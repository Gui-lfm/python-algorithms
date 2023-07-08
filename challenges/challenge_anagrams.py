def is_anagram(first_string: str, second_string: str):
    first_string = first_string.lower()
    second_string = second_string.lower()

    first_sorted = merge_sort(first_string)
    second_sorted = merge_sort(second_string)

    if first_sorted == "" or second_sorted == "":
        return (first_sorted, second_sorted, False)

    if first_sorted == second_sorted:
        return (first_sorted, second_sorted, True)
    return (first_sorted, second_sorted, False)


def merge_sort(string: str):
    if len(string) <= 1:
        return string

    middle = len(string) // 2
    left = string[:middle]
    right = string[middle:]

    sort_left = merge_sort(left)
    sort_right = merge_sort(right)

    return merge(sort_left, sort_right)


def merge(left, right):
    result = ""
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result += left[i]
            i += 1
        else:
            result += right[j]
            j += 1

    result += left[i:]
    result += right[j:]

    return result


print(is_anagram('amor', 'roma'))