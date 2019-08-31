import os, urllib.request

data_dir = r'/home/danielz/Documents'

pages = [

    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},

    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },

    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]

##i=0
##while i < len(pages):
##    try:
##        path = os.path.join(data_dir, pages[i]['name']+'.html')
##        print(path)
##        urllib.request.urlretrieve(pages[i]['url'], path)
##        i+=1
##    except:
##        print('An error appeared !')
##        break
##else:
##    print('The processing finished succesfully')
##                    

for page in pages:
 
    try:
        file_name = "{}.html".format(page["name"])
        path = os.path.join(data_dir, file_name)
 
        print("Processing: {}  => {} ...".format(page["url"], file_name))
        urllib.request.urlretrieve (page["url"], path)
        print('...done')
        
    except:
        print('FAILURE processing web page: {}'.format(page["name"]))
        print('Stopping the process!')
        break
 
else:
    print('All pages downloaded successfully!!!')
