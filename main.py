def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def get_words_count(file_str):
    number_of_words = file_str.split()
    return len(number_of_words)

def main():
    book_contents = get_book_text("books/frankenstein.txt")
    word_count = get_words_count(book_contents)
    print(f"{word_count} words found in the document")

main()
