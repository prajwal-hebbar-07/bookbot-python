from stats import get_words_count, get_character_count
from read_book import get_book_text
from sys import argv, exit


def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    book_title = argv[1]
    book_contents = get_book_text(book_title)
    word_count = get_words_count(book_contents)
    character_count = get_character_count(book_contents)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_title}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for key, value in character_count.items():
        print(f"{key}: {value}")


main()
