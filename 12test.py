import os



path= r'/home/danielz/Documents/file.txt'
os.remove(path)

result =  os.path.isfile(path) or open(path, 'x').close()

print(result)
