__author__ = 'leihuang'

def square(x):
    '''
    Square a number and returns the result

    >>> square(2)
    4
    >>> square(3)
    9

    :param x:
    :return: x*x
    '''
    return x*x

if __name__ == '__main__':
    import doctest, doctest_demo
    doctest.testmod(doctest_demo)
