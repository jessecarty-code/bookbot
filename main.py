import sys
from stats import get_num_words
from stats import get_num_char
from stats import sort_on
from stats import letters_sort

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1] 
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters_dict = get_num_char(text)
    sorted_list = letters_sort(letters_dict)
    print_report(book_path, num_words, sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
