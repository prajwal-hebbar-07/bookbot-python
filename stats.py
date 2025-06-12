def get_words_count(file_str):
    number_of_words = file_str.split()
    return len(number_of_words)


def get_character_count(file_str):
    lowercase_file_str = file_str.lower()
    character_count = {}

    for char in lowercase_file_str:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count
