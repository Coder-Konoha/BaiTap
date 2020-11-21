"""n = int(input("Nhập n: "))
tong = 0
i = 1
while i <= n:
    tong +=i
    i +=1
print("Tổng các số từ 1 tới", n, "là", tong)"""
n = int(input("Nhập n: "))
tong = 0
for i in range(0, n+1):
    tong +=i
print("Tổng các số từ 1 tới", n, "là", tong)