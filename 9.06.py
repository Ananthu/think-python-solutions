

with open('words.txt', 'r') as fd:
    word_list = fd.read().split()


def is_abecedarian(word):
    return word == ''.join(sorted(word))

words = [word for word in word_list if is_abecedarian(word)]

print "There are {} abecedarian words.".format(len(words))
