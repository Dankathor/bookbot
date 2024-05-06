
def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    print(text)
    word_count = count_words(text)
    print(word_count)

def get_text(path):
    with open(path) as f:
        return f.read()

def count_words(book_text):
    words = book_text.split()
    return len(words)

main()