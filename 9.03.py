

word = str("steven")
string = str("qx")


def avoids(word, string):
    for letter in string:
        if letter in word:
            return False
    return True

print avoids(word, string)
