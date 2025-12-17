from stats import count_words, count_chars, sort_for_printing

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content
    
def main():
    print("============ BOOKBOT ============")

    path = "books/frankenstein.txt"

    print(f"Analyzing book found at {path}...")

    content = get_book_text(path)
    word_count = count_words(content)

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    

    char_counts = count_chars(content)
    sorted_counts = sort_for_printing(char_counts)

    print("--------- Character Count -------")
    
    for count in sorted_counts:
        print(f"{count["char"]}: {count["num"]}")
    
    print("============= END ===============")

main()