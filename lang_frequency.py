import sys
from collections import Counter
from re import findall


def load_data(file_path):
    words_in_file = findall(r'\w+', open(file_path).read().lower())
    return words_in_file


def get_most_frequent_words(words_in_file):
    most_frequent_words = Counter(words_in_file).most_common(10)
    return most_frequent_words


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        words_in_file = load_data(file_path)
    except FileNotFoundError:
        sys.exit('Файл не найден, попробуйте еще раз.')
    except IndexError:
        sys.exit('Используйте синтакс: "python lang_frequency.py <filename>"')
    most_frequent_words = get_most_frequent_words(words_in_file)
    for word, qty in most_frequent_words:
        print(word)