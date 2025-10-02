import sys
from stats import get_num_words, count_characters, count_sorted_characters


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(path)} total words")
    print("--------- Character Count -------")
    char_freq = count_sorted_characters(path)
    for dictionary in char_freq:
        print(f"{dictionary['name']}: {dictionary['num']}")
    print("============= END ===============")


main()
