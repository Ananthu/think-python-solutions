


import os

cwd = os.getcwd()
names = []

def walk(directory):
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isfile(path):
            names.append(path)
        else:
            walk(path)
    print names

walk(cwd)


