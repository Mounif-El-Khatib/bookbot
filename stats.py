def get_book_text(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def get_num_words(filepath: str):
    text = get_book_text(filepath)
    return len(text.split())


def count_characters(filepath: str):
    frequency_map = {}
    text = get_book_text(filepath)

    for c in text:
        if c.lower() not in frequency_map:
            frequency_map[c.lower()] = 1
        else:
            frequency_map[c.lower()] += 1

    return frequency_map


def sort_on(items):
    return items["num"]


def count_sorted_characters(filepath: str):
    frequency_map = count_characters(filepath)
    sorted_freq_map = []
    for key, value in frequency_map.items():
        if key == " ":
            continue
        temp_map = {"name": key, "num": value}
        sorted_freq_map.append(temp_map)
    sorted_freq_map.sort(reverse=True, key=sort_on)
    return sorted_freq_map
