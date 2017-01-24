import os
import shutil

path = r"C:/Users/li/Desktop/posts/"
path2 = r"C:/Users/li/Desktop/posts2/"
files = []
sizes = []
dels = []
for ii in range(3, 13531):
    fileName = path + str(ii) + ".html"
    if os.path.exists(fileName):
        size = os.path.getsize(fileName)
        files.append(ii)
        sizes.append(size)
        dels.append(False)

for ii in range(0, len(files)):
    for jj in range(ii + 1, len(files)):
        if sizes[ii] == sizes[jj]:
            dels[ii] = True
            dels[jj] = True
        else:
            break

for ii in range(0, len(files)):
    print(files[ii], sizes[ii], dels[ii])
    if not dels[ii]:
        file1 = path + str(files[ii]) + ".html"
        file2 = path2 + str(files[ii]) + ".html"
        shutil.copy(file1, file2)