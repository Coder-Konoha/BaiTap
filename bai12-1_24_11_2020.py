import random
A=[]
B=[]
#1 - Tạo 1 số nguyên ngẫu nhiên n trong khoảng [50, 1000] đóng vai trò là số phần tử của List
n = random.randint(50, 1000)
#2 - Sinh ngẫu nhiên 1 List các số nguyên trong khoảng [-1000, 1000]
for i in range(n):
    A.append(random.randint(-1000,1000))
#3 - Sinh ngẫu nhiên 1 List các số thực trong khoảng [-1000.0, 1000.0]
for i in range(n):
    B.append(random.uniform(-1000.0,1000.0))