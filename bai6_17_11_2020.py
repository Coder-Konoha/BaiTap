import random
import math
n = int(input("Nhập n phần tử số thực cần đưa vào list: "))
A = []
gtmax = -math.inf
for a in range(n):
    A.append((random.uniform(-n, n)))
print (A)
for i in A:
    if i > gtmax:
        gtmax = i
print ("Giá trị lớn nhất là:", gtmax)