import sys

from stats import (
    chars_dict_to_sorted_list,
    get_chars_dict,
    get_num_words,
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_chars_dict(text)
    sorted_char_counts = chars_dict_to_sorted_list(char_counts)
    print_report(book_path, num_words, sorted_char_counts)


def print_report(
    book_path: str,
    num_words: int,
    sorted_char_counts: list[tuple[str, int]],
) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_char_counts:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()