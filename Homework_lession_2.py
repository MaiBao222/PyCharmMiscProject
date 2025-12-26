import random
import math
import platform
#bai 1
a = random.randint(1, 10)
b = random.randint(1, 10)
print("Số thứ nhất: ", a)
print("Số thứ hai: ", b)
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b
can_tich = math.sqrt(tich)
print("Tổng: ", tong)
print("Hiệu: ", hieu)
print("Tích: ", tich)
print("Thương: %.2f" % (thuong))
print("Căn bậc hai của tích: %.2f" % (can_tich))
#bai 2
point_1 = (random.randint(1,100), random.randint(1,100))
point_2 = (random.randint(1,100), random.randint(1,100))
x = point_2[0] - point_1[0]
y = point_2[1] - point_1[1]
space = math.hypot(x, y)
print(point_1, point_2)
print('Khoảng cách 2 điểm ngẫu nhiên: %.2f' % space)
#bai 3
xx1 = random.randint(1,6)
xx2 = random.randint(1,6)
xx3 = random.randint(1,6)
tong = xx1 + xx2 + xx3
print('tổng điểm 3 xúc xắc: ', tong)
if tong % 2 == 0:
    print('là số chắn => căn bậc 2: %.2f' % math.sqrt(tong))
else:
    print('là số lẻ => bình phương: %.2f' % math.pow(tong, 2))
#bai 4
print(platform.system())
print(platform.processor())
print(platform.version())
print(platform.platform())
num_1 = random.randint(1,100)
num_2 = random.randint(1,100)
print('hai số ngẫu nhiên: ', num_1, num_2)
tong = num_1 + num_2
hieu = num_1 - num_2
tich = num_1 * num_2
thuong = num_1 / num_2
list_kq = [('tổng:',tong), ('hiệu:',hieu), ('tich:',tich), ('thuong:',thuong)]
print(random.sample(list_kq, 3))
#bai 5
num_choice = random.randint(1, 50)
for i in range(1, 6):
    num_input = int(input(f'Nhập lần {i}: '))
    if num_input < num_choice:
        print('Số trúng thưởng LỚN hơn số bạn đoán')
    elif num_input > num_choice:
        print('Số trúng thưởng NHỎ hơn số bạn đoán')
    else:
        print(f'Chúc mừng bạn. Số trúng thưởng là: {num_choice}')
        print(platform.platform)
        print('căn bậc 2 của số đúng: %.2f' % (math.sqrt(num_choice)))
        break
else:
    print('Bạn đã thua')
    print(f'Số trúng thưởng là: {num_choice}')