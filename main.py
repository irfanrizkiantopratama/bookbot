
# print report
# pasang url tersebut lalu assign ke variable baru kemudian panggil dengan function yang sudah di set
# parameter nya 

# count words
# masukan file yang tersebut lalu parse agar bisa membaca total angka nya berapa

# count letters
# print a report

def main():
    bookpath = "books/frankenstein.txt"
    text = get_the_book(bookpath)
    num_words = get_the_numbers(text)
    char_dict = get_char(text)
    chars_sorted_list = chars_dict_to_sorted_list(char_dict)

    print(f"-- Begin report of {bookpath} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} time")
    print("--- end report ---")

def get_the_book(path):  # untuk menghasilkan book
    with open(path) as f:
        return f.read()

def get_the_numbers(text): #untuk split book
    words = text.split()
    return len(words)

def get_char(text): 
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] +=1
        else:
            chars[lowered] = 1
    return chars

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]


main()
