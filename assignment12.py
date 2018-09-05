# q.1 print the current day

import datetime 
p=datetime.datetime.now()
print(p.day)


# q.2 use webbrowser module in python

import webbrowser as web
web.open("https://www.google.com")


# q.3 rename all the files in a directory and convert them into .jpg file format

import os
path = '\Users\Prateek\Downloads\Programs'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.jpg'))
    i = i+1
