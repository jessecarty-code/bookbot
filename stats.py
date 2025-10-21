def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(items):
    return items["num"]

def get_num_char(text):
    letters_dict = {}
    for i in text.lower():
        if i in letters_dict:
            letters_dict[i] += 1
        else:
            letters_dict[i] = 1
    return letters_dict

def letters_sort(letters_dict):
    letters_sort = []
    for ch in letters_dict:
        letters_sort.append({"char":ch, "num": letters_dict[ch]})
    letters_sort.sort(reverse=True, key=sort_on)
    return letters_sort
