class HtmlCM:

    def __init__(self, filename, mode, Number, Description):
        self.filename = filename
        self.mode = mode
        self.Number = Number
        self.Description = Description

    def __enter__(self):
        import os
        dir = os.getcwd()
        self.f = open(os.path.join(dir, self.filename), self.mode)
        self.f.write(
"""<table>
    <tr>
        <th>{}</th><th>{}</th>
    </tr>
""".format(self.Number, self.Description)
        )

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.f.write("</table>")
        self.f.close()

import os, subprocess

with HtmlCM("index.txt", 'w', 1, "Hello") as f:
    path = os.path.join(os.getcwd(), 'index.html')
    # subprocess.call(['open', path])
    # os.system("start index.html")
    #subprocess.call(("start index.html"))
    os.system('open'+" "+path)



