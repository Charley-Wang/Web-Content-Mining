import re

f = open("C:/Users/li/Desktop/certificate.txt", "r")
lines = f.readlines()
f.close()

dict = {}
p = re.compile(r"\b[A-Z]{2,}\b|\b[A-Z]+.*?[A-Z]+\b]")
for line in lines:
    ress = p.findall(line)
    for res in ress:
        if res in dict.keys():
            dict[res] += 1
        else:
            dict[res] = 1

pp = ""
for key in dict.keys():
    if pp == "":
        pp = key
    else:
        pp += "|" + key

p1 = re.compile(pp)
p5 = re.compile(r"\b[A-Z][a-zA-Z0-9]+?\b [A-Z][a-zA-Z0-9]+?\b [A-Z][a-zA-Z0-9]+?\b [A-Z][a-zA-Z0-9]+?\b [A-Z][a-zA-Z0-9]+?\b")
p4 = re.compile(r"\b[A-Z][a-zA-Z0-9]+?\b [A-Z][a-zA-Z0-9]+?\b [A-Z][a-zA-Z0-9]+?\b [A-Z][a-zA-Z0-9]+?\b")
p3 = re.compile(r"\b[A-Z][a-zA-Z0-9]+?\b [A-Z][a-zA-Z0-9]+?\b [A-Z][a-zA-Z0-9]+?\b")
p2 = re.compile(r"\b[A-Z][a-zA-Z0-9]+?\b [A-Z][a-zA-Z0-9]+?\b")
dict2 = {}
for line in lines:
    line = p1.sub("", line)

    res5 = p5.findall(line)
    for res51 in res5:
        p52 = re.compile(res51)
        line = p52.sub("", line)
        if res51 in dict2.keys():
            dict2[res51] += 1
        else:
            dict2[res51] = 1

    res4 = p4.findall(line)
    for res41 in res4:
        p42 = re.compile(res41)
        line = p42.sub("", line)
        if res41 in dict2.keys():
            dict2[res41] += 1
        else:
            dict2[res41] = 1

    res3 = p3.findall(line)
    for res31 in res3:
        p32 = re.compile(res31)
        line = p32.sub("", line)
        if res31 in dict2.keys():
            dict2[res31] += 1
        else:
            dict2[res31] = 1

    res2 = p2.findall(line)
    for res21 in res2:
        p22 = re.compile(res21)
        line = p22.sub("", line)
        if res21 in dict2.keys():
            dict2[res21] += 1
        else:
            dict2[res21] = 1

for key in dict:
    print(str(dict[key]) + " *** " + key)

for key in dict2:
    print(str(dict2[key]) + " *** " + key)