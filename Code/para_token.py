from urllib.request import urlopen
import math
import re
import urllib
import webbrowser
import glob
import os
import shutil

def get_skills():
    fileName = "C:\\Users\\li\\Desktop\\freq_good.dat"
    f = open(fileName, "r")
    lines = f.readlines()
    f.close()

    rep2 =  r"\bc\+\+|\bc\+\+[ ,.;?&()\"']"
    rep2 += r"|\bc#|\bc#[ ,.;?&()\"']"
    rep2 += r"|\bc/c\+\+|\bc/c\+\+[ ,.;?&()\"']"
    rep2 += r"|\.net\b|[ ,.;?&()\"']\.net\b"

    for line in lines:
        txts = line.split()
        rep2 += r"|\b" + txts[1].strip().lower() + r"\b"

    return rep2

def search_skills(fileName, texts):
    rep = r"skill|experience|certification|education|qualifications|requirements"
    rep += r"|educational instruction in|expertise in|ability to|able to|knowledge of|familiarity with"
    rep += r"|understanding of|management of|knowledge in"
    rep += r"|candidates .*? possess|candidates .*? have|candidates .*? be"
    rep += r"|is .*? desired|are .*? desired|is .*? required|are .*? required|preferred"
    rep += r"|bachelor|master|doctoral| bs | ms | phd |degree"
    rep += r"|must possess|must have|must be"
    rep += r"|clearance|citizen"
    rep += r"|" + get_skills()

    p = re.compile(rep)
    nums = []
    for text in texts:
        nums.append(len(p.findall(text.lower())))

    l = len(texts)
    moving_sum_5 = []
    left_4 = []
    right_4 = []
    pt = []
    for ii in range(l):
        pt.append(0)
        beg1 = max(0, ii - 4)
        left = 0
        for jj in range(beg1, ii):
            left += nums[jj]
        left_4.append(left)

        end1 = min(ii + 5, l)
        right = 0
        for jj in range(ii + 1, end1):
            right += nums[jj]
        right_4.append(right)

        num = 0
        beg1 = max(0, ii - 2)
        end1 = min(ii + 3, l)
        for jj in range(beg1, end1):
            num += nums[jj]
        moving_sum_5.append(num)

    beg2 = 0
    end2 = 0
    for ii in range(l):
        if nums[ii] >= 1 and moving_sum_5[ii] >= 2 and right_4[ii] >= 2:
            beg2 = ii
            break
        if nums[ii] >= 3:
            beg2 = ii
            break

    for ii in range(beg2 + 1, l):
        if nums[ii] >= 1 and moving_sum_5[ii] >= 2 and left_4[ii] >= 2:
            end2 = ii
        if nums[ii] >= 3:
            end2 = ii

    #if beg2 == 0 and end2 == 0:
    #    print(fileName)
    #else:
    #    path = r"C:/Users/li/Desktop/posts3/"
    #    path2 = r"C:/Users/li/Desktop/posts6/"
    #    file1 = path + fileName
    #    file2 = path2 + fileName
    #    shutil.copy(file1, file2)

    if end2 == 0:
        end2 = l - 1

    print("==================")
    print(fileName)
    print("------------------")
    for ii in range(beg2, end2):
        print(ii, nums[ii], texts[ii])

#get_skills("")
#exit()

path = r"C:/Users/li/Desktop/posts6/"
os.chdir(path)
files = glob.glob("*.html")

num = 0
for file in files:
    num += 1
    if num >= 500:
        continue
    fileName = path + file
    f = open(fileName, "r")
    lines = f.readlines()
    p1 = re.compile(r"\\r|\\n|\\t|&nbsp;|\\x..")
    p2 = re.compile(r"<.*?>")
    p3 = re.compile(r"&amp;")
    p4 = re.compile(r"{")
    p5 = re.compile(r"\b.+?\b")
    texts = []
    for line in lines:
        paras = p2.split(line)
        for para in paras:
            para = p1.sub("", para)
            para = p3.sub("&", para)
            para = para.strip()
            if len(p4.findall(para)) >= 1:
                continue
            if len(p5.findall(para)) <= 4:
                continue
            if len(para) <= 3:
                continue
            texts.append(para)

    # search skills paragraph
    search_skills(file, texts)

    #break

