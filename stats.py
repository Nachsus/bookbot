def count_words(file_content):
    return len(file_content.split())

def count_chars(file_content):
    lowered = file_content.lower()
    char_counts = {}
    chars = list(lowered)
    unique_chars = list(set(chars))
    for char in unique_chars:
        char_counts[char] = 0

    for char in chars:
        char_counts[char] += 1

    return char_counts

def sort_on(items):
    return items["num"]

def sort_for_printing(char_counts_dict):
    combs = []
    for key, value in char_counts_dict.items():
        new_dict = {
            "char": key,
            "num": value
        }
        combs.append(new_dict)

    combs.sort(reverse=True, key=sort_on)

    return combs