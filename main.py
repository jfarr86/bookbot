def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(num_words)
    chars_dict = get_chars_dict(text)
    print(chars_dict)
    print_report(book_path)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len (words)

def get_chars_dict(text : str) -> dict:
    chars = {}
    text = text.lower()
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def dict_to_list(dict):
    list = []
    for key in dict:
        if key.isalpha():
            list.append({"char": key, "num": dict[key]})
    return list

def sort_on(dict):
    return dict["num"]
    
def print_report(path):
    print(f"--- Begin report of {path} ---")
    text = get_book_text(path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document\n")
    
    chars_dict = get_chars_dict(text)
    chars_list = dict_to_list(chars_dict)
    chars_list.sort(reverse=True, key=sort_on)
    for item in chars_list:
        print(f"The '{item["char"]}' character was found {item["num"]} times")
    print("--- End report ---")
    
    
    
main()