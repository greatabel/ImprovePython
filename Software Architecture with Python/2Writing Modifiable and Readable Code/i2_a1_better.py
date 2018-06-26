# 

""" Module A - Implement functions that operate on series of numbers """

#
def squares(narray):
    return pow_n(narray, 2)

def cubes(narray):
    return pow_n(narray, 3)

def pow_n(narray, n):
    return [pow(x, n) fox x in narray]

# def frequency(string, word):
#     word_l = word.lower()
#     string_l = string.lower()

#     words = string_l.split()
#     count = w.count(word_l)
#     return 100 * count / len(words)