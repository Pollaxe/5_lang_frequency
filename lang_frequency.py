import sys
from collections import Counter
from re import findall


def load_data(file_path):
    words_in_file = findall(r'\w+', open(file_path).read().lower())
    return words_in_file


def get_ten_most_frequent_words(words_in_file):
    most_frequent_words_limit = 10
    most_frequent_words = Counter(words_in_file).most_common(most_frequent_words_limit)
    return most_frequent_words


def print_most_frequent_words(most_frequent_words):
    for word, qty in most_frequent_words:
        print(word)


if __name__ == '__main__':
    file_path = sys.argv[1]
    try:
        words_in_file = load_data(file_path)
    except FileNotFoundError:
        sys.exit('Файл не найден, попробуйте еще раз.')
    except IndexError:
        sys.exit('Используйте синтакс: "python lang_frequency.py <filename>"')
    most_frequent_words = get_ten_most_frequent_words(words_in_file)
    print_most_frequent_words(most_frequent_words)