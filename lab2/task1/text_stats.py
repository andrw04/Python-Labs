from collections import namedtuple
from functools import reduce


def read_file(path):
    text = ''
    with open(path, 'r') as file:
        text = file.read()

    return text


def is_word(text):
    return text.isalnum() and not text.isdigit()


def get_all_words(text):
    words = text.split(' ')
    words = [word.strip(r',.:;?!\'"(){}') for word in words]
    words = [word for word in words if is_word(word)]

    return words


def amount_sentences(text):
    pass


def amount_non_declarative(text):
    pass


def average_word_length(text):
    words = get_all_words(text)

    all_word_length = reduce(lambda a, b: a + len(b), words, 0)

    return round(all_word_length / len(words), 3)


def average_sentence_length(text):
    pass


def top_repeated(text,k=10, n=4):
    pass


def calculate(text):
    pass



def main():
    path = 'lab2/task1/text.txt'
    text = read_file(path)
    count = average_word_length(text)
    print(count)


if __name__ == '__main__':
    main()