from urllib.request import urlopen
import math
import re
import urllib
import webbrowser
import glob
import os

url = "http://www.enlabel.com/careers/software-development-engineer"

html = urlopen(url).read().decode("utf-8")
pattern1 = re.compile('\n')
text = pattern1.sub('', html)
pattern1_2 = re.compile(r' &amp; ')
text = pattern1_2.sub(' and ', text)
pattern1_3 = re.compile('(\\\\x..)')
text = pattern1_3.sub('', text)
print("------------")
#print(text)
print("============")


sock = urlopen(url)
htmlSource = sock.read()
sock.close()
#print(htmlSource)

f = open(r"C:\Users\li\Desktop\posts\temp2.html", "w")
#htmlSource = re.sub('\\\\x\d\d', '', htmlSource)
f.writelines("%s" % htmlSource)
f.close()
