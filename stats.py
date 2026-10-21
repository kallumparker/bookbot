def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_chars_dict(text: str) -> dict[str, int]:
    chars: dict[str, int] = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(char_count: tuple[str, int]) -> int:
    return char_count[1]


def chars_dict_to_sorted_list(
    char_counts: dict[str, int],
) -> list[tuple[str, int]]:
    sorted_list: list[tuple[str, int]] = []
    for char in char_counts:
        sorted_list.append((char, char_counts[char]))
    return sorted(sorted_list, key=sort_on, reverse=True)
