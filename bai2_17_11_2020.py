"""n = int(input("Số lần giải phương trình: "))
i = 1
while i <= n:
    a = float(input("Nhập vào hệ số a: "))
    b = float(input("Nhập vào hệ số b: "))
    if a==0:
        if b==0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
        i += 1
    else:
        x = -b/a 
        print("Nghiệm của phương trình là x =", x)
        i += 1"""
n = int(input("Số lần chương trình được giải: "))
for i in range(1, n+1):
    a = float(input("Nhập vào hệ số a: "))
    b = float(input("Nhập vào hệ số b: "))
    if a==0:
        if b==0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -b/a 
        print("Nghiệm của phương trình là x =",x)