import random
import math
#Tạo một List gồm cấc số thực (có thể tạo bằng tay hoặc ngẫu nhiên)
n = int(input("Nhập n phần tử số thực cần đưa vào list: "))
tl = int(input("1. Tạo list bằng tay\n2. Tạo list random\nLựa chọn: "))
pt = 1
A = []
if tl == 1:
    for a in range(n):
        A.append(float(input("Nhập số thứ %d: " %(a+1))))
if tl == 2:
    for a in range(n):
        A.append(random.uniform(-n, n))
#Lặp truy xuất đến từng phần tử trong List và in giá trị của từng phần tử ra màn hình
for i in A:
    print("Phần tử thứ %d:" %pt, i)
    pt += 1
else:
    pt = 1
#Lặp truy xuất đến từng phần tử trong List và thực hiện tính logarith của từng phần tử và in giá trị đó ra màn hình
for i in A:
    if i > 0:
        print("Logarith của phần tử thứ %d:" %pt, math.log10(i))
        pt += 1
    else:
        print("Không thể tính logarith của phần tử thứ %d" %pt)
        pt += 1