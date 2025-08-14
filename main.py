import sys
from stats import word_count, dict_to_array

def sort_on(item):
    return item["num"]

def get_book_text(title):    
    with open(f"{title}") as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)

    # Passed as CLI argument    
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at ${path}...")
    print("----------- Word Count ----------")

    text = get_book_text(path)
    num_words = word_count(text)

    print(f"Found {num_words} total words")
    print("--------- Character Count -------")


    chars = dict_to_array(text)
    chars.sort(reverse=True, key=sort_on)

    for i in range(0, len(chars)):
       if chars[i]["name"].isalpha():
        print(f"{chars[i]["name"]}: {chars[i]["num"]}")

main()
