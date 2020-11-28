import random
n = int(input("Nhập n phần tử số thực cần đưa vào list: "))
A = []
for a in range(n):
    A.append((random.uniform(-n, n)))
gtmax = A[0]
gtmin = A[0]
for i in A[1:]:
    if i > gtmax:
        gtmax = i
for i in A[1:]:
    if i < gtmin:
        gtmin = i