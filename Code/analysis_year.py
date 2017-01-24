import re

f = open("C:/Users/li/Desktop/year.txt", "r")
lines = f.readlines()
f.close()

fout = open("C:/Users/li/Desktop/year2.txt", "w")

p1 = re.compile(r"year")
p2 = re.compile(r"(\d{1,2})-(\d{1,2})")

pp = r"(\d{1,2}|one|two|three|four|five|six|seven|eight|nine|ten|twelve|twenty)"
pp += r"( |\+|\+ | \+| \+ |-|- |\) | or more | plus ||\+\)|\+\) ||\) or more |\) additional | additional| additional "
pp += r"|  |\)|\+  |plus |\)\+ "
pp += r")year"
p3 = re.compile(pp)

p4 = re.compile("per year|00 /year")

for line in lines:
    line = line.lower()

    if len(p4.findall(line)) > 0:
        continue

    total = len(p1.findall(line))

    res2 = p2.findall(line)

    for res in res2:
        txt = res[0] + "-" + res[1]
        p5 = re.compile(txt)
        line = p5.sub("", line)

        n1 = int(res[0])
        n2 = int(res[1])
        n = (n1 + n2)/2.0
        txts = line.split("***")
        fout.write(txts[0] + str(n) + "\n")

    res3 = p3.findall(line)
    for res in res3:
        txt = res[0]
        if txt == "one":
            n = 1
        elif txt == "two":
            n = 2
        elif txt == "three":
            n = 3
        elif txt == "four":
            n = 4
        elif txt == "five":
            n = 5
        elif txt == "six":
            n = 6
        elif txt == "seven":
            n = 7
        elif txt == "eight":
            n = 8
        elif txt == "nine":
            n = 9
        elif txt == "ten":
            n = 10
        elif txt == "twelve":
            n = 12
        elif txt == "twenty":
            n = 20
        else:
            n = int(txt)
        txts = line.split("***")
        fout.write(txts[0] + str(n) + "\n")

fout.close()