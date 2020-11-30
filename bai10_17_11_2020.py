import numpy as np
import pandas as pd
import matplotlib as mpl 
import matplotlib.pyplot as plt
#1. Numpy
#Tạo ma trận
A = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]]) 
B = np.array([[1, 3, 5], [7, 9, 11], [13, 15, 17]])
#Tổng 2 ma trận
print(A + B)
#Tích 2 ma trận
print(A.dot(B))
#Chuyển vị ma trận
print(A.transpose())
print(B.transpose())
#2. Pandas
#Đọc dữ liệu từ file excel (dạng csv) trên máy tính vào bộ nhớ và in ra 10 dòng đầu tiên
ex1 = pd.read_csv(r'C:\NhatMinh\GitHub\Coder-Konoha\BaiTap\EPL.csv')
print(ex1.head(10))
#Đọc dữ liệu từ file excel (dạng csv) trên mạng Internet vào bộ nhớ và in ra 10 dòng đầu tiên
ex2 = pd.read_csv('https://raw.githubusercontent.com/Coder-Konoha/BaiTap/main/EPL.csv')
print(ex2.head(10))
#Đọc dữ liệu từ file có định dạng JSON (tren mạng internet) vào bộ nhớ và in ra 10 dòng đầu tiên
ex3 = pd.read_json('https://api.github.com/users/voduytuan/repos')
print(ex3.head(10))
#3. Matplotlib
#Tạo biểu đồ char
plt.bar(ex1.iloc[:, 1], ex1.iloc[:, -1], align = 'center', width = 0.8, color='green')
plt.title('Point EPL season 2020-2021 round 10 ')
plt.xlabel('CLB')
plt.ylabel('Points')
plt.show()
#Tạo biểu đồ line
mun_gf = [83, 80, 68, 86, 78, 89, 86]
che_gf = [64, 65, 68, 103, 69, 65, 75]
season = ['2006-07', '2007-08', '2008-09', '2009-10', '2010-11', '2011-12', '2012-13']
plt.plot(season, mun_gf, color = 'red')
plt.plot(che_gf, color = 'blue')
plt.title("GF Manchester United & Chelsea from seasons 2006 - 2013")
plt.xlabel('Seasons')
plt.ylabel('Goal For')
plt.show()
#Tạo biểu đồ Boxplot
x = np.random.randn(100) + np.arange(0, 100) * 0.5
y = np.random.randn(100) + np.arange(0, 100) * 1.0 + 10
z = np.random.randn(100) + np.arange(0, 100) * 2 - 15
plt.boxplot([x, y, z], labels = ['x', 'y', 'z'], showfliers = True)
plt.title('Boxplot')
plt.xlabel('Classes')
plt.ylabel('x, y, z')
plt.show()