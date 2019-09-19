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
        if exc_type == FileNotFoundError:
            print("Except_type: {}".format(exc_type))
            print("Except_value: {}".format(exc_value))
            print("Except_traceback: {}".format(exc_traceback))
            return True
        elif exc_type == KeyError:
            print("Except_type: {}".format(exc_type))
            print("Except_value: {}".format(exc_value))
            print("Except_traceback: {}".format(exc_traceback))
            return True
        else:
            return False

url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip"
path = os.path.join(os.getcwd(), 'eurofxref.zip')

with FileFromWeb(url, path) as ffw:
    with zipfile.ZipFile(ffw.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir("/home/daniel/Documents/Gitprojects/Python_intermediate/extract")
        z.extract(a_file, ".", pwd=None)

