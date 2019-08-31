
text_list = ['x','xxx','xxxxx','xxxxxxx','']

n = 'dowolny napis'

f = lambda x : len(x)

print(f(n))

print(list(map(f, text_list)))
print(list(map(lambda x: len(x), text_list)))
