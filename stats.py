def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
def word_count(text):
    return len(text.split())
def char_count(text):
    frequency = {}
    freq_list = []
    for letter in text.lower():
        if letter not in frequency:
            frequency[letter] = 1
        else:
            frequency[letter] += 1
    for key in frequency:
        freq_list.append({"letter": key, "count": frequency[key]})
    return freq_list

