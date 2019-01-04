import os

# a template string.. could'be improved
template_string="""<!DOCTYPE html>
 <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
         body{font-family:  'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;font-size: 0.8rem; background-color:   #448AFF;}
        body a {
            display:block;text-decoration: none; color: #000;
            padding: 10px 10px 10px 30px;
            background-color:white;
           
            -webkit-box-shadow: 2px 2px 6px -1px rgba(50,65,235,0.86);
-moz-box-shadow: 2px 2px 6px -1px rgba(50,65,235,0.86);
box-shadow: 2px 2px 6px -1px rgba(50,65,235,0.86);

            }
    </style>
</head>
<body>
"""
dirs = os.listdir()

# filtering the directories only

dirs = list(filter((lambda m: len(m.split('.'))==1),dirs))
file = open('index.html',"wt")
file.write(template_string)

# creating links
folders  = list(map((lambda i:"""<a href = '{0}/index.html' >{1}</a><br>""".format(i,i[3:])),dirs))

for i in folders:
    file.write(i)
    
    
# function which creates all the index files on sub-directories

def create_index(path):
    os.chdir(path)
    print("Currently in {}".format(os.getcwd()))
    files = os.listdir()
    file = open('index.html','wt')
    file.write(template_string)
    dirs  = list(map((lambda i:"""<a href = '{0}'target='_blank'>{1}</a><br>""".format(i,i[3:])),files))
    for i in dirs:
        file.write(i)
    file.write("""</body>
</html>""")
    os.chdir('../')
    print("Currently in {}".format(os.getcwd()))
    

    
for i in dirs:
    create_index(os.path.join(os.getcwd(),i))
