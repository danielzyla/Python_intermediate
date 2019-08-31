files_to_process = [
    r"/home/danielz/Documents/Python/Python dla sredniozaawans/math_sin_square.py",
    r"/home/danielz/Documents/Python/Python dla sredniozaawans/math_square_root.py"
    ]

for path in files_to_process:
##    with open(path) as file:
##        source = file.read()
##        #print(source)
##        exec(source)
    with open(path, 'r') as f:
        print("File {} ...".format(path))
        source = f.read()
        exec(source)
