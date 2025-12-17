def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content
    
def count_words(file_content):
    return len(file_content.split())
    
def main():
    path = "books/frankenstein.txt"
    content = get_book_text(path)
    word_count = count_words(content)
    print(f"Found {word_count} total words")

main()