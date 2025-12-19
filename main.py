import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]

from stats import get_num_words, count_characters, sort_char_counts 

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

def main():
    text = get_book_text(path_to_book)
    word_count = f"Found {get_num_words(text)} total words" 
    print(word_count)

    character_count = count_characters(text)


    sorted_chars = sort_char_counts(character_count)
    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        if not char.isalpha():
            continue
        print(f"{char}: {num}")



main()