import os
tenthumuc = str(input('Nhập tên thư mục: '))
tentaptin = str(input('Nhập tên tệp tin: '))
os.mkdir('C:\%s' %tenthumuc)
os.chdir('C:\%s' %tenthumuc)
open(tentaptin, 'x')