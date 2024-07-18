def main():
    path_to_file = "./books/frankenstein.txt"
    text = get_text(path_to_file)
    print_report(path_to_file)


def count_characters(text):
    chars = {}
    
    for c in text:
        lowered = c.lower()

        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars


def count_words(text):
    words = text.split()
    return len(words)


def get_text(path):
    with open(path) as f:
        return f.read()


def print_report(path):
    def sort_on(dict):
        return dict["count"]


    text = get_text(path)
    dx = count_characters(text)

    print(f"--- Begin report of {path} ---")
    words = count_words(text)
    print(f"{words} words found in the document")
    print()

    char_list = [{"char": char, "count": count} for char, count in dx.items()]
    char_list.sort(reverse=True, key=sort_on)


    for d in char_list:
        if d["char"].isalpha():
            print(f"The '{d['char']}' character was found {d['count']} times")

    print("--- End report ---")



main()
        














