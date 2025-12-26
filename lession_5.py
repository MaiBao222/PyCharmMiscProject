# ký tự - character
# mã ký tự - unicode
# ASCII - bảng mã
# mã UTF-8
# tìm hiểu 2 hàm ord() và chr ()
# một số ký tự đặc biệt với dấu \ - Escape
# text = "Aeにほ漢"
# print(text)
# for ch in text:
#     print(ch)
# for ch in text:
#     print(ord(ch)) # trả về ký tự dạng số nguyên code point
# for ch in text:
#     print(hex(ord(ch))) # mã hex
# # chuyển từ codepoint sang ký tự
# print(chr(12395),chr(12396),chr(12397),chr(12398))
# # thống nhất các ký tự phổ biến vào 1 bộ
# name = 'Mai Bảo'
# enc = name.encode('utf-8')
# dec = enc.decode('utf-8')
# print(enc)
# print(dec)
# a = str(input('nhap ky tu: '))
# for i in a:
#     print('codepoint:', ord(i))
# from Buoi_3_BT import list_2

# 1 số toán tử so sánh
# so sánh nội dung  của 2 chuỗi, ký tự
# for b in range(1,20):
#     print('*' * (b))

# tình huống: nhập vào đoạn chữ và in ra các ký tự có dấu
# a = str(input('nhap ky tu: '))
# for i in a:
#     b = ord(i)
#     if b > 127:
#         print(b,'là chữ:',chr(b))

# Unicode: 1 triệu ký tự !!!!
# ASCII: 0-127 thể hiện bảng chữ cái latinh
# in ra bảng ký tụ ascII
# for i in range (0,32):
#     print(chr(i))
# for i in range (32,128):
#     print(chr(i))

# một số bài tập thực hành
# chuyển chuỗi từ có dấu sang không dấu




