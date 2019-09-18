import os
import requests

dir = os.getcwd()

def gen_get_files(dir):
    for file in os.listdir(dir):
        yield os.path.join(dir, file)


# for path in gen_get_files(dir):
#     print(path) 

def gen_get_file_lines(filename):
    f = open(os.path.join(dir, filename))
    for line in f:
        if line.endswith('\n'):
            yield line.replace('\n', '')
        else:
            yield line

# for text in gen_get_file_lines(filename):
#     print(text)

def check_webpage(url):
    try:
        r=requests.get(url)
        if r.status_code == 200:
            return True
    except requests.exceptions.ConnectionError:
        return False

print(check_webpage(url))

try:
    dir_with_links = os.path.join(dir,'links_to_check')
    os.mkdir(dir_with_links)
except:
    pass
    
with open(os.path.join(dir_with_links, 'pl.txt'), 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
    f.write('http://www.demotywatory.pl')
    
with open(os.path.join(dir_with_links, 'com.txt'), 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')


for file in gen_get_files(dir_with_links):
    for line in gen_get_file_lines(file):
        print('{} - {} - {}'.format(file, line, check_webpage(line)))