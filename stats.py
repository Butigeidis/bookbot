def word_count(text):
    split_text = text.split()
    return len(split_text)

def char_count(text):
    dict = {}
    for symbol in text:
        symbol = symbol.lower()
        if symbol not in dict:
            dict[symbol] = 1
        else:
            dict[symbol] += 1

    return dict

def dict_to_array(text):
    collection = []
    chars = char_count(text)
    for char in chars:
        collection.append({"name": char, "num": chars[char]})
    return collection

        