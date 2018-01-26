import sys


def load_data(file_path):
    with open(file_path) as content:
        text = content.read()
    return text


def get_most_frequent_words(text):
    most_frequent_words = dict()
    most_frequent_words_list = []
    for word in text.split():
        if word not in most_frequent_words:
            most_frequent_words[word] = 1, word
        else:
            buffer = most_frequent_words[word][0]+1
            most_frequent_words[word] = buffer, word
    for word in most_frequent_words:
        most_frequent_words_list += [(most_frequent_words[word])]
    list.sort(most_frequent_words_list, key=lambda x: (-x[0], x[1]))
    return most_frequent_words_list


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        text = load_data(file_path)
    except FileNotFoundError:
        sys.exit('Файл не найден, попробуйте еще раз.')
    except IndexError:
        sys.exit('Используйте синтакс: "python lang_frequency.py <filename>"')
    most_frequent_words_list = get_most_frequent_words(text)
    for word in range(10):
        try:
            print(most_frequent_words_list[word][1])
        except IndexError:
            sys.exit()
