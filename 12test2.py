import os

def readfile(filepath):
    file=open(filepath,'r')
    text=file.read()
    txtsplitted=text.split()
    return print('There are %d words in the file'%(len(txtsplitted)))


path = r'/home/danielz/Documents/file.txt'

if os.path.isfile(path):
    readfile(path)

result = os.path.isfile(path) and readfile(path)
