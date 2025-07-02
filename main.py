import sys
from stats import get_num_words, count_characters, sort_char_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    char_counts = count_characters(text)
    sorted_char_counts = sort_char_counts(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in sorted_char_counts:
        print(f"{char}: {count}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()