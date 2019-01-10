import os

# a template string.. could'be improved
template_string="""<!DOCTYPE html>
 <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href='https://fonts.googleapis.com/css?family=Alfa Slab One' rel='stylesheet'>
    <title>Your List</title>
    <style>
         body{font-family:  'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;font-size: 0.8rem; background: linear-gradient(0.1turn, #52aefb, #8e0bb4, #eb0bb4);}
        .snowflake {
  color: #fff;
  font-size: 1em;
  font-family: Arial, sans-serif;
  text-shadow: 0 0 5px #000;
}

@-webkit-keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}@-webkit-keyframes snowflakes-shake{0%,100%{-webkit-transform:translateX(0);transform:translateX(0)}50%{-webkit-transform:translateX(80px);transform:translateX(80px)}}@keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}@keyframes snowflakes-shake{0%,100%{transform:translateX(0)}50%{transform:translateX(80px)}}.snowflake{position:fixed;top:-10%;z-index:9999;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:default;-webkit-animation-name:snowflakes-fall,snowflakes-shake;-webkit-animation-duration:10s,3s;-webkit-animation-timing-function:linear,ease-in-out;-webkit-animation-iteration-count:infinite,infinite;-webkit-animation-play-state:running,running;animation-name:snowflakes-fall,snowflakes-shake;animation-duration:10s,3s;animation-timing-function:linear,ease-in-out;animation-iteration-count:infinite,infinite;animation-play-state:running,running}.snowflake:nth-of-type(0){left:1%;-webkit-animation-delay:0s,0s;animation-delay:0s,0s}.snowflake:nth-of-type(1){left:10%;-webkit-animation-delay:1s,1s;animation-delay:1s,1s}.snowflake:nth-of-type(2){left:20%;-webkit-animation-delay:6s,.5s;animation-delay:6s,.5s}.snowflake:nth-of-type(3){left:30%;-webkit-animation-delay:4s,2s;animation-delay:4s,2s}.snowflake:nth-of-type(4){left:40%;-webkit-animation-delay:2s,2s;animation-delay:2s,2s}.snowflake:nth-of-type(5){left:50%;-webkit-animation-delay:8s,3s;animation-delay:8s,3s}.snowflake:nth-of-type(6){left:60%;-webkit-animation-delay:6s,2s;animation-delay:6s,2s}.snowflake:nth-of-type(7){left:70%;-webkit-animation-delay:2.5s,1s;animation-delay:2.5s,1s}.snowflake:nth-of-type(8){left:80%;-webkit-animation-delay:1s,0s;animation-delay:1s,0s}.snowflake:nth-of-type(9){left:90%;-webkit-animation-delay:3s,1.5s;animation-delay:3s,1.5s}.snowflake:nth-of-type(10){left:25%;-webkit-animation-delay:2s,0s;animation-delay:2s,0s}.snowflake:nth-of-type(11){left:65%;-webkit-animation-delay:4s,2.5s;animation-delay:4s,2.5s}
        .box{
            margin-top: 5%;
            margin-left: 4%;
            margin-right: 4%;
            padding-top: 10%;
            padding-left: 20%;
            padding-right: 20%;
            padding-bottom: 10%;
            border-style: solid;
            border-width: 2px;
            border-color: #c50b72;
            border-radius: 8px;
            font-size: 150%;
            background: linear-gradient(0.1turn, #d7df73, #f4c073, #0097ba);
        }
        .inner_box{
            margin-top: 2%;
            padding: 2%;
            height: 30%;
            max-height: 30%;
            border-style: solid;
            border-width: 2px;
            border-color: #c50b72;
            color: #02d8fc;
            border-radius: 4px;
            margin-bottom: 2%;
            background: linear-gradient(0.1turn, #52aefb, #8e0bb4, #eb0bb4);
        }
        .inner_box:hover{
            box-shadow:
                1px 1px #7d8d89,
                3px 3px #7d8d89,
                5px 5px #7d8d89;
            -webkit-transform: translateX(-3px);
            transform: translateX(-3px);
        }
    </style>
</head>
<body>
 <div class="snowflakes" aria-hidden="true">
  <div class="snowflake">
  ❅
  </div>
  <div class="snowflake">
  ❆
  </div>
  <div class="snowflake">
  ❅
  </div>
  <div class="snowflake">
  ❆
  </div>
  <div class="snowflake">
  ❅
  </div>
  <div class="snowflake">
  ❆
  </div>
  <div class="snowflake">
    ❅
  </div>
  <div class="snowflake">
    ❆
  </div>
  <div class="snowflake">
    ❅
  </div>
  <div class="snowflake">
    ❆
  </div>
  <div class="snowflake">
    ❅
  </div>
  <div class="snowflake">
    ❆
  </div>
</div>

<div class="box">
 <center style="background: -webkit-linear-gradient(0.1turn, #52aefb, #8e0bb4, #eb0bb4); background: -o-linear-gradient(0.1turn, #52aefb, #8e0bb4, #eb0bb4); background: -moz-linear-gradient(0.1turn, #52aefb, #8e0bb4, #eb0bb4); background: linear-gradient(0.1turn, #52aefb, #8e0bb4, #eb0bb4); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-family: 'Alfa Slab One';font-size: 150%;"><u>VideoPlayer Online</u></center><br>
"""
dirs = os.listdir()

# filtering the directories only

dirs = list(filter((lambda m: len(m.split('.'))==1),dirs))
file = open('index.html',"wt")
file.write(template_string)

# creating links
folders  = list(map((lambda i:"""<div class='inner_box'><a href = '{0}/index.html' style='text-decoration: none;color: white;'><b>{1}</b></a></div>""".format(i,i[3:])),dirs))

for i in folders:
    file.write(i)
    
    
# function which creates all the index files on sub-directories

def create_index(path):
    os.chdir(path)
    print("Currently in {}".format(os.getcwd()))
    files = os.listdir()
    file = open('index.html','wt')
    file.write(template_string)
    dirs  = list(map((lambda i:"""<div class='inner_box'><a href = '{0}'target='_blank' style='text-decoration: none;color: white;'><b>{1}</b></a></div>""".format(i,i[3:])),files))
    for i in dirs:
        file.write(i)
    file.write("""</div></body>
</html>""")
    os.chdir('../')
    print("Currently in {}".format(os.getcwd()))
    

    
for i in dirs:
    create_index(os.path.join(os.getcwd(),i))
