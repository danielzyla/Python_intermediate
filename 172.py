import os, zipfile, requests
from zipfile import ZipFile

class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self):
        response = requests.get(self.url)
        print(response)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip"
path = os.path.join(os.getcwd(), 'eurofxref.zip')

with FileFromWeb(url, path) as ffw:
    with zipfile.ZipFile(ffw.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        z.extract(a_file, "/home/daniel/Documents/Gitprojects/Python_intermediate/extract", pwd=None)

