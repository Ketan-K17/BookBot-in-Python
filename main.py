
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    # print(f"Word count of book : {num_words} words.")
    num_letters = get_num_letters(book_text)
    # print("Count of each letter in book...")
    # print(num_letters)
    show_result(book_path, num_words, num_letters)

def get_num_letters(book_text):
    book_text = book_text.lower()
    all_letter_counts = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    for i in range (0, len(book_text)):
        if book_text[i].isalpha(): # checks if given character is alphabet or not.
            all_letter_counts[book_text[i]] += 1

    return all_letter_counts


def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        book_text = f.read()
    return book_text

def get_num_words(book_text):
    word_list = book_text.split()
    return len(word_list)

def show_result(book_path, num_words, num_letters):
    print(f"Beginning report of {book_path}...")
    print(f"{num_words} words found in document")
    print("\n")
    sorted_counts = sorted(num_letters.items(), key=lambda x: x[1], reverse=True)

    for letter, count in sorted_counts:
        print(f"The '{letter}' character was found {count} times")

    print("\n---End of report---")



main()