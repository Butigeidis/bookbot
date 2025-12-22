import sys
from stats import get_book_text, word_count, char_count

def sort_on(items):
    return items["count"]

def is_letter(symbol):
    return (symbol >= "A" and symbol <= "Z") or (symbol >= "a" and symbol <= "z")

def main():
    if len(sys.argv) < 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count(text)} total words")
    print("--------- Character Count -------")
    
    list = char_count(text)
    my_list = list.sort(reverse=True, key=sort_on)
    for individual_obj in list:
        if individual_obj["count"] >= 1 and is_letter(individual_obj["letter"]):
            print(f"{individual_obj["letter"]}: {individual_obj["count"]}") 
    
main()