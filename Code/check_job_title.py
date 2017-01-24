import os
import glob

path = r"C:/Users/li/Desktop/posts6/"
os.chdir(path)
files = glob.glob("*.html")

titleFile = "C:/Users/li/Desktop/jobs_20151111.txt"
outputFile = "C:/Users/li/Desktop/jobs_20151111_last_used.txt"
f = open(titleFile, "r")
lines = f.readlines()

fout = open(outputFile, "w")

for line in lines:
    txts = line.split(",")
    txt = txts[0] + ".html"
    if txt in files:
        out = txts[0] + "," + txts[2] + "," + txts[3] + "\n"
        fout.write(out)

fout.close()
