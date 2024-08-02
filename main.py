def count_words(text):
    words = text.split()
    return len(words)

def count_chars(book_text):
    lower_text = book_text.lower()
    character_count = {}

    for char in lower_text:
        if char.isalpha():
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1

    character_list = [{'char': char, 'count': count} for char, count in character_count.items()]
    return character_list

def main():
    with open('./books/frankenstein.txt') as f:
        book_text = f.read()
        
    return_dict = count_chars(book_text)
    return_dict.sort(key=lambda x: x['count'], reverse=True)
    print(return_dict)

main()