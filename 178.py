import os, requests
from zipfile import ZipFile
from contextlib import closing, suppress

class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def download_file(self):
        response = requests.get(self.url)
        print(response)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self
    
    def close(self):
        #if os.path.isfile(self.tmp_file):
        os.remove(self.tmp_file)
        #pass

url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip"
path = os.path.join(os.getcwd(), 'eurofxref.zip')

with suppress(FileNotFoundError):
    with closing(FileFromWeb(url, path)) as ffw:
        ffw.download_file()
        with ZipFile(ffw.tmp_file, 'r') as z:
            a_file = z.namelist()[0]
            print(a_file)
            os.chdir("/home/daniel/Documents/Gitprojects/Python_intermediate/extract")
            z.extract(a_file, ".", pwd=None)
            os.remove(ffw.tmp_file)

