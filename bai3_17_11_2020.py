#a.	Lặp và in ra từng ký tự của chữ
for kytu in "Konoha":
    print("Ký tự hiện tại:", kytu)

#b.	Lặp qua phần tử của từng mảng
Anti_Mage = ["Tread", "Fury", "Manta", "Abyssal", "Butterfly", "BKB"]
n=1
for item in Anti_Mage:
    print("Item AM slot %d:" %n, item)
    n += 1

#c.	Tìm ra các số nguyên tố từ trong một list a được nhập từ bàn phím
def songuyento(number):
    if(number<2):
        return False
    i = 2
    while i <= number/2:
        if(number%i == 0):
            return False
        i += 1
    return True
n = int(input("Nhập n số cần đưa vào list: "))
A = []
for a in range(n):
    A.append(int(input("Nhập số thứ %d: " %(a+1))))
A = list(dict.fromkeys(A))
print("Các số nguyên tố gồm:")
for i in A:
    if(songuyento(i)):
        print(i, end = " ")

#3.	Thay đổi bước nhảy của từng bước lặp
print("Các số chẵn từ 0 đến 20:")
for i in range(0, 20, 2):
    print(i, end = " ")
    print("\nCác số lẻ từ 0 đến 20:")
for i in range(1, 20, 2):
    print(i, end = " ")

#Vd:
for i in range(0, 51, 5):
    print(i, end = " ")

#4.	Kết hợp vòng lặp for với hàm range và len
Anti_Mage = ["Tread", "Fury", "Manta", "Abyssal", "Butterfly", "BKB"]
n=1
for item in range(len(Anti_Mage)):
    print("Item AM slot %d:" %n, Anti_Mage[item])
    n += 1

#5.	Kết hợp vòng lặp for với else, break, continue
a = int(input("Nhập giá trị bắt đầu: "))
b = int(input("Nhập giá trị kết thúc: "))
for x in range (a, b) :
    print("Giá trị của x = ", x)
    #break (Hoặc là break)
    #continue (Hoặc là continue)
if x >= max(range(a, b)):
    print("Đã đạt giá trị lớn nhất")
else:
    print("Có", len(range(a, b)), "giá trị")
    print("Giá trị nhỏ nhất là:", min(range(a, b)))
    print("Giá trị lớn nhất là:", max(range(a, b)))
    print("Kết thúc")