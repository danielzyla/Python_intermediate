import os
import itertools as it

def scantree(path):
    with os.scandir(path) as p:
        for entry in p:
            if entry.is_dir():
                yield ('dir', entry.name)
                #for i in scantree(entry):
                    #yield i
            else:
                yield ('file', entry.name)

path = os.getcwd()

listing = scantree(path)
print(listing)

listing = sorted(listing, key= lambda x: x[0])
print('-'*20)
print(listing)
# for k, g in it.groupby(data , lambda x: x[0]):
#     print('The key is {} and elements are {}'.format(k, list(g)))

for k, g in it.groupby(listing , key=lambda x: x[0]):
    print('The key is {} and elements amount is {}'.format(k, len(list(g))))
