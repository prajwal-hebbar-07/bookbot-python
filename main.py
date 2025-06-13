from stats import get_words_count, get_character_count
from read_book import get_book_text


def main():
    book_title = "frankenstein.txt"
    book_contents = get_book_text(f"books/{book_title}")
    word_count = get_words_count(book_contents)
    character_count = get_character_count(book_contents)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{book_title}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for key, value in character_count.items():
        print(f"{key}: {value}")


main()
