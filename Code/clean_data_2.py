from urllib.request import urlopen
import math
import re
import urllib
import webbrowser
import glob
import os
import shutil

path = r"C:/Users/li/Desktop/posts2/"
path2 = r"C:/Users/li/Desktop/posts3/"
os.chdir(path)
files = glob.glob("*.html")

for file in files:
    f = open(path + file, "r")
    lines = f.readlines()
    save = False
    p = re.compile(r"computer science")
    for line in lines:
        line = line.lower()
        if len(p.findall(line)) > 0:
            save = True
            break
    if save:
        file1 = path + file
        file2 = path2 + file
        shutil.copy(file1, file2)
        print(file)

