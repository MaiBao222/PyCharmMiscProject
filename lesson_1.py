# Buổi số 1 :
# module và package trong Python
# Đóng gói, tách câu lệnh thành thư viện, 1 file độc lập
# cho dễ quản lý
# cách tổ chức dự án Python init , pycache , name ....
# thực hành viết module riêng, tạo package .....

#import cal
#print(cal.div(2,3))

#from cal import add
#print(add(1,2))

#import cal as ca
#print(ca.div(2,3))

#from demo import add
#print(add(2,3))

#import cal
#print(dir(cal))
#import sys
#print(sys.path)

#from demo_1 import *
#print(add(2,3))
#print(sub(2,3))

#from convester import conv as cv
#print(cv.met(2000),'km')
#print(int(cv.tem(37)),'độ F')

import strings_operations as so
print(so.reverse_string('Hello World'))
print(so.count_vowels('Hello World'))
print(so.remove_space('Hello World'))

from geometry import point as p
x1 = int(input('toạ độ x1: '))
y1 = int(input('toạ độ y1: '))
x2 = int(input('toạ độ x2: '))
y2 = int(input('toạ độ y2: '))
space = p.distance((x1,y1),(x2,y2))
print('khoảng cách: %.2f' % space)