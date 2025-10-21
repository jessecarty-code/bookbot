def get_book_text(b):
    contents = b.read()
    return contents

with open("books/frankenstein.txt") as b:
    content = get_book_text(b)
    words = content.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

