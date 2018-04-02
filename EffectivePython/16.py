__author__ = 'leihuang'

def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index+1

addres = 'four and three year'
result = list(index_words_iter(addres))
print result
