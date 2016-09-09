
with open('words.txt', 'r') as fd:
    word_list = fd.read().split()


def uses_all(word, string):
    count = 0
    for letter in string:
        if letter in word:
            count += 1
    if count == len(string):
        return True
    return False


def find_uses_all_vowels(list):
    count = 0
    string = 'aeiou'
    for word in list:
        if uses_all(word, string):
            count += 1
    return count

print find_uses_all_vowels(word_list)


