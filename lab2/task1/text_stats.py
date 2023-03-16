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
    words = [word.lower() for word in words if is_word(word)]

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
    words = get_all_words(text)
    words = [word for word in words if len(word) == 4]

    word_count = {}

    for word in words:
        if word not in word_count.keys():
            word_count[word] = 1
        else:
            word_count[word] += 1
    
    sorted_word = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    top_k_repeated = {}

    for key, value in sorted_word:
        if k == 0:
            break
        
        top_k_repeated[key] = value

    return top_k_repeated



def calculate(text):
    pass



def main():
    path = 'text.txt'
    text = read_file(path)
    count = average_word_length(text)
    print(top_repeated(text))
    #print(count)


if __name__ == '__main__':
    main()