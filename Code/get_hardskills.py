from urllib.request import urlopen
import math
import re
import urllib
import webbrowser
import glob
import os
import shutil

def create_dict_hard_skill():
    fileName = "C:\\Users\\li\\Desktop\\hardskills_used.dat"
    f = open(fileName, "r")
    lines = f.readlines()
    f.close()

    dict = {}
    for line in lines:
        txts = line.lower().split(",")
        dict[txts[1].strip()] = 0

    return dict

def get_skills_locate():
    fileName = "C:\\Users\\li\\Desktop\\freq_good.dat"
    f = open(fileName, "r")
    lines = f.readlines()
    f.close()

    rep = r"skill|experience|certification|education|qualifications|requirements"
    rep += r"|educational instruction in|expertise in|ability to|able to|knowledge of|familiarity with"
    rep += r"|understanding of|management of|knowledge in"
    rep += r"|candidates .*? possess|candidates .*? have|candidates .*? be"
    rep += r"|is .*? desired|are .*? desired|is .*? required|are .*? required|preferred"
    rep += r"|bachelor|master|doctoral| bs | ms | phd |degree"
    rep += r"|must possess|must have|must be"
    rep += r"|clearance|citizen"

    rep2 = rep + r"|\bc\+\+|\bc\+\+[ ,.;?&()\"']"
    rep2 += r"|\bc#|\bc#[ ,.;?&()\"']"
    rep2 += r"|\bc/c\+\+|\bc/c\+\+[ ,.;?&()\"']"
    rep2 += r"|\.net\b|[ ,.;?&()\"']\.net\b"

    for line in lines:
        txts = line.split()
        rep2 += r"|\b" + txts[1].strip().lower() + r"\b"

    return rep2

def search(texts, rep2_locate, dict_soft, dict_soft_data, data_added):
    p = re.compile(rep2_locate)
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

    if end2 == 0:
        end2 = l - 1

    for ii in range(beg2, end2):
        text = texts[ii]
        for key in dict_soft:
            key1 = key[0:1]
            key2 = key[len(key)-1:len(key)]
            pp = r""
            if key1.isalpha():
                pp += r"\b"
            pp += key
            if key2.isalpha():
                pp += r"\b"
            # print(pp)
            p = re.compile(pp)
            if len(p.findall(text)) > 0:
                dict_soft[key] += 1
                if data_added:
                    dict_soft_data[key] += 1

    return [dict_soft, dict_soft_data]

def get_data_file_index():
    fileName = "C:/Users/li/Desktop/jobs_20151111_last_used.txt"
    f = open(fileName, "r")
    lines = f.readlines()

    search =  r"\bdata\b|\bbi\b|\bmachine learning\b|\bbusiness intelligence\b"
    search += r"|\bbusiness .*?analyst\b|\bsap\b.*?analyst\b|\bmarketing .*?analyst\b"
    search += r"|\binformatics .*?analyst\b|\bstatistical\b"
    search += r"|\bsecurity .*?analyst\b|\bproduct .*?analyst\b|\bservices .*?analyst\b|\brisk .*?analyst\b|\bsas\b"
    p1 = re.compile(search)

    num = 0
    nums = []
    for line in lines:
        line = line.lower()
        if len(p1.findall(line)) > 0:
            num += 1
            txts = line.split(",")
            nums.append(int(txts[0]))

    return nums

# ===================================================================================
# main program

# exit()

path = r"C:/Users/li/Desktop/posts6/"
os.chdir(path)
files = glob.glob("*.html")

rep2_locate = get_skills_locate()
dict_soft = create_dict_hard_skill()
dict_soft_data = create_dict_hard_skill()
data_index = get_data_file_index()

print(dict_soft)

num = 0
for file in files:
    num += 1
    fileNum = int(file[0:len(file) - 5])

    print(num, file, fileNum)

    data_added = False
    if fileNum in data_index:
        data_added = True

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

    res = search(texts, rep2_locate, dict_soft, dict_soft_data, data_added)
    dict_soft = res[0]
    dict_soft_data = res[1]

for key in dict_soft:
    print(key, "*", dict_soft[key], "*", dict_soft_data[key])
