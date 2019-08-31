import requests 
import os
import functools
    
def save_url_file(msg, url, dir, file):
        
    print(msg.format(file))
    
    r = requests.get(url, stream = True) 
    file_path = os.path.join(dir, file)
        
    with open(file_path, "wb") as f: 
        f.write(r.content)


msg = "Please wait - the file {} will be downloaded"
    
url = 'http://mobilo24.eu/spis'
dir = '/home/danielz/Documents'
file = 'spis.html'
#save_url_file(url, dir, file,msg)
'''  
url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
dir = '/home/danielz/Documents'
file = 'logo.png'
'''
#save_url_file(url, dir, file,msg)

save_url_to_dir = functools.partial(save_url_file, msg, url)
save_url_to_dir(file=file, dir=dir)