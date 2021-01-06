'''
1. Thư viện thao tác tập tin, thư mục và các hàm cơ bản:
Thư viện os, pathlib, shutil,...
Các hàm cơ bản:
open(fileName, mode), mode bao gồm:(r, r+, w, w+, a, a+)
.read([size])
.readline([size])
.write(fileName)
.close()
os.name
os.getcwd()
os.popen()
os.close()
os.rename()
os.access()
os.listdir()
os.mkdir()
os.path.exists()
os.remove()
os.rmdir
............
'''
import os
asd = 'C:\\'
list1 = []
list2 = []
for root, dirs, files in os.walk(asd):   #Lập trình đọc tất cả tập tin và thư mục con trực tiếp của thư mục gốc ổ đĩa C
    list1.append(files) #quest3
    list2.append(dirs) #quest3
    break
print(list2, list1) #quest2
