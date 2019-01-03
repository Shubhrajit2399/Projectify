import os
template_string="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        body{background-color: #FAFAFA;}
        body a {text-decoration: none; color: #7FC4EE;padding-left:1rem; padding-top:10px; padding-right:5px;padding-bottom:10px; }
    </style>
</head>
<body>"""
dirs = os.listdir()

dirs = list(filter((lambda m: len(m.split('.'))==1),dirs))
file = open('index.html',"wt")
file.write(template_string)
folders  = list(map((lambda i:"""<a href = '{0}/index.html'>{1}</a><br>""".format(i,i[3:])),dirs))

for i in folders:
    file.write(i)
    
    

def create_index(path):
    os.chdir(path)
    print("Currently in {}".format(os.getcwd()))
    files = os.listdir()
    file = open('index.html','wt')
    file.write(template_string)
    dirs  = list(map((lambda i:"""<a href = '{0}'>{1}</a><br>""".format(i,i[3:])),files))
    for i in dirs:
        file.write(i)
    file.write("""</body>
</html>""")
    os.chdir('../')
    print("Currently in {}".format(os.getcwd()))
    

    
for i in dirs:
    create_index(os.path.join(os.getcwd(),i))
