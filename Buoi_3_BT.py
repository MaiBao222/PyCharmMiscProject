# #bai 1
# while True:
#     try:
#         a = int(input("Enter a: "))
#         b = int(input("Enter b: "))
#         result = a / b
#     except ValueError as e:
#         print("loi kieu du lieu")
#     except ZeroDivisionError as e:
#         print("Phep chia cho 0")
#     except Exception as e:
#         print("Co loi xay ra vui long thu lai")
#     else:
#         print("a/b = %.2f" % (result))
#         break
# #bai_2
# number_list = [10,20,30,40,50]
# while True:
#     try:
#         number_list = [10, 20, 30, 40, 50]
#         b = int(input('nhập vị trí muốn truy xuất: '))
#         print(f'tại index {b} giá trị =', number_list[b])
#     except IndexError as x:
#         print('vị trí truy xuất không hợp lệ - ', x)
#     except ValueError as y:
#         print('vị trí truy xuất là số không phải chữ - ', y)
#     else:
#         print('done')
#         break
# #bai_3
# try:
#     with open("number.txt", "r") as f:
#         total = 0
#         for line in f:
#             line = line.strip()
#             if line == "":
#                 continue
#             try:
#                 num = float(line)
#                 total += num
#             except ValueError:
#                 print(f"Dòng không hợp lệ (bỏ qua): {line}")
#         print(f"Tổng các số hợp lệ: {total}")
# except FileNotFoundError:
#     print("Lỗi: File 'numbers.txt' không tồn tại.")
# finally:
#     print("Hoàn tất chương trình.")
# #bai_4
# while True:
#     try:
#         list_1 = list(map(float, input('Nhap chuoi so: ').split()))
#         print('gia tri trung binh: %.2f' % (sum(list_1)/len(list_1)))
#     except ValueError as e:
#         print("loi kieu du lieu")
#     except ZeroDivisionError:
#         print('loi chia cho 0')
#     else:
#         print('done')
#         break
# #bai_5
# while True:
#     try:
#         list_2 = list(map(str, input('nhap du lieu: ').strip().split()))
#         print(list_2)
#         for i in list_2:
#             a = str(i)
#     except ValueError:
#         print('Bắt các lỗi nhập sai kiểu dữ liệu')
#     else:
#         break
# while True:
#     try:
#         b = int(input('nhập vị trí muốn truy xuất: '))
#         print(f'tai vi tri {b}:', list_2[b])
#         list_2.append(input('them phan tu: '))
#         print(list_2)
#     except ValueError as e:
#         print("Bắt các lỗi nhập sai kiểu dữ liệu")
#     except IndexError as e:
#         print("truy cập ngoài phạm vi")

