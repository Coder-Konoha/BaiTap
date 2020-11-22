import random
import math
n = int(input("Nhập n phần tử số thực cần đưa vào list: "))
A = []
for a in range(n):
    A.append((random.uniform(-n, n)))
gtmax = A[0]
gtmin = A[0]
print (A)
for i in A[1:]:
    if i > gtmax:
        gtmax = i
print("Giá trị lớn nhất là:", gtmax)
for i in A[1:]:
    if i < gtmin:
        gtmin = i
print("Giá trị nhỏ nhất là:", gtmin)