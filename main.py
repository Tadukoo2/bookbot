import sys
from typing import Any
from stats import get_num_words, get_num_characters, generate_report

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path: str = sys.argv[1]
    book_text: str = get_book_text(book_path)
    num_words: int = get_num_words(book_text)
    # print(f"{num_words} words found in the document")
    char_counts: dict[str, int] = get_num_characters(book_text)
    # print(f"{char_counts}")
    characters: list[dict[str, Any]] = generate_report(char_counts)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...")
    print(f"----------- Word Count ----------\nFound {num_words} total words")
    print("--------- Character Count -------")
    for character_map in characters:
        character: str = character_map.get("character")
        if not character.isalpha():
            continue
        number: int = character_map.get("number")
        print(f"{character}: {number}")
    print("============= END ===============")

main()
