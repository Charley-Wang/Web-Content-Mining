from urllib.request import urlopen
import math
import re
import urllib
import webbrowser
import glob
import os

path = r"C:/Users/li/Desktop/postings/"
os.chdir(path)
files = glob.glob("*.html")

f = open("C:/Users/li/Desktop/jobs_20151111.txt", "w")

ii = 0
for file in files:
    print("===========" + file)
    url = r"file:///" + path + file

    # html = urlopen(r"file:///C:/Users/li/Desktop/postings/1.html").read().decode("utf-8")
    html = urlopen(url).read().decode("utf-8")
    pattern1 = re.compile('\n')
    text = pattern1.sub('', html)
    pattern1_2 = re.compile(r' &amp; ')
    text = pattern1_2.sub(' and ', text)
    pattern1_3 = re.compile(r'(\u201A|\xb8|\xe2|\u20ac|\xc3|\xa2|\u200f)')
    text = pattern1_3.sub('', text)

    pattern2 = re.compile('<div class=".*?row.*?result".+?</div>')
    results = pattern2.findall(text)

    for result in results:
        pattern3 = re.compile('data-tn-element="jobTitle">(.+?)</a>')
        jobTitle = pattern3.findall(result)
        if len(jobTitle) == 0:
            continue

        pattern4 = re.compile('<a rel=".+?" href="(.+?)" target')
        href = pattern4.findall(result)
        if len(href) == 0:
            continue
        pattern4_2 = re.compile('(master|computer|science)')
        res = pattern4_2.findall(href[0])
        if len(res) >= 3:
            continue

        pattern5 = re.compile('<span itemprop="name">(.+?)</span>')
        company = pattern5.findall(result)
        if len(company) == 0:
            continue

        pattern6 = re.compile('<span itemprop="addressLocality">(.+?)</span>')
        location = pattern6.findall(result)
        if len(location) == 0:
            continue

        ii += 1

        pattern7 = re.compile(r',')
        jobTitle = pattern7.sub(' ', jobTitle[0])
        pattern7 = re.compile(r',')
        company = pattern7.sub(' ', company[0].strip())
        pattern7 = re.compile(r' ([A-Z][A-Z])')
        state = pattern7.findall(location[0].strip())

        pattern7 = re.compile(r' {2,}')
        jobTitle = pattern7.sub(' ', jobTitle)
        pattern7 = re.compile(r' {2,}')
        company = pattern7.sub(' ', company)

        print(ii)
        print(location)
        print(state)
        if len(state) == 0:
            state = location[0]

        f.write(str(ii) + ",")
        f.write(file + ",")
        f.write(jobTitle + ",")
        f.write(state[0] + ",")
        f.write(company + ",")
        f.write(href[0] + "\n")

f.close()




