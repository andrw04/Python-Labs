import os
from functools import reduce
import re


def read_file(path):
    if os.path.exists(path):
        text = ''
        with open(path, 'r') as file:
            text = file.read()
        return text
    else:
        return None


def is_word(text):
    return text.isalnum() and not text.isdigit()


def get_all_words(text):
    words = text.split(' ')
    words = [word.strip(r',.:;?!\'"(){}') for word in words]
    words = [word.lower() for word in words if is_word(word)]

    return words


def get_all_sentences(text):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)

    return sentences


def amount_sentences(text):
    sentences = get_all_sentences(text)

    return len(sentences)


def amount_non_declarative(text):
    sentences = get_all_sentences(text)
    count = 0
    for sentence in sentences:
        if '!' in sentence or '?' in sentence:
            count += 1

    return count


def average_word_length(text):
    words = get_all_words(text)
    if not len(words):
        return 0

    all_word_length = reduce(lambda a, b: a + len(b), words, 0)

    return round(all_word_length / len(words), 3)


def average_sentence_length(text):
    sentences = get_all_sentences(text)
    average = 0

    for sentence in sentences:
        average += len(sentence)

    average /= len(sentences)
    
    return average


def top_repeated(text,k=10, n=4):
    words = get_all_words(text)
    words = [word for word in words if len(word) == n]

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
        k -= 1

    return top_k_repeated


def main():
    abs_file_path = os.path.abspath(__file__)
    path, file_name = os.path.split(abs_file_path)
    path = os.path.join(path, 'text.txt')
    text = read_file(path)
    sent_amount = amount_sentences(text)
    non_declarative = amount_non_declarative(text)
    av_w_len = average_word_length(text)
    av_sent_len = average_sentence_length(text)
    print(f"Amount of sentences: {sent_amount}")
    print(f"Amount of non-declarative sentences: {non_declarative}")
    print(f"Average word length: {av_w_len}")
    print(f"Average senteces length: {av_sent_len}")


if __name__ == '__main__':
    main()