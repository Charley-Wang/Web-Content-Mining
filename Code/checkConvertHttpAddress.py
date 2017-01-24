import glob
import re
from urllib.request import urlopen
import math
import urllib
import webbrowser
import os

files = glob.glob("C:\\Users\\li\\Desktop\\post\\*.txt")

for file in files:
    f = open(file, "r")
    lines = f.readlines()
    f.close()

    con = 1
    num = int(len(lines) / 3)
    for ii in range(num):
        n = lines[ii*3].strip()
        print(n)
        if int(n) <= 4207:
            continue
        old = lines[ii*3 + 1]
        new = lines[ii*3 + 2]
        if not n.isdigit():
            print(file)
            print(n)
            con = 0
            continue
        pattern = re.compile(r"http")
        if len(pattern.findall(old)) == 0:
            print(file)
            print(n)
            print("old is not right.")
            con = 0
            continue
        if len(pattern.findall(new)) == 0:
            print(file)
            print(n)
            print("new is not right.")
            con = 0
            continue

        try:
            sock = urlopen(new)
            htmlSource = sock.read()
            sock.close()
            fname = "C:\\Users\\li\\Desktop\\posts\\" + n + ".html"
            f = open(fname, "w")
            f.writelines("%s" % htmlSource)
            f.close()
        except:
            print("wrong in: ", n)
