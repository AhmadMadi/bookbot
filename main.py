from collections import Counter

def count_words(text):
    """Counts the number of words in a given text."""
    words = text.split()
    return len(words)

def count_chars(book_text):
    """Counts the occurrences of each character in the given text and returns a sorted list."""
    lower_text = book_text.lower()
    character_count = Counter(char for char in lower_text if char.isalpha())

    character_list = [{'char': char, 'count': count} for char, count in character_count.items()]
    character_list.sort(key=lambda x: x['count'], reverse=True)
    return character_list

def main():
    """Reads the text from a file, counts characters, and prints the sorted list of character counts."""
    with open('./books/frankenstein.txt') as f:
        book_text = f.read()
        
    sorted_char_counts = count_chars(book_text)
    print(sorted_char_counts)

if __name__ == "__main__":
    main()