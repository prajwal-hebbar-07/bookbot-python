from stats import get_words_count
from read_book import get_book_text


def main():
    book_contents = get_book_text("books/frankenstein.txt")
    word_count = get_words_count(book_contents)
    print(f"{word_count} words found in the document")


main()
