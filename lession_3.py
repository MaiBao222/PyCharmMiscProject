#XỬ LÝ NGOẠI LỆ
#áp dụng try except mức độ cơ bản
# try:
#     sub = 4/0
# except Exception as e:
#     print("Có lỗi xảy ra: ", e)

#áp dụng try except mức độ trung bình
# try:
#     a = int(input("Enter a: "))
#     b = int(input("Enter b: "))
#     result = a/b
# except Exception as e:
#     print("có lỗi xảy ra")
# else:
#     print("a/b=", result)
# finally:
#     print('Xong')

# def device(a,b):
#     try:
#         result = a / b
#     except ValueError as e:
#         print("loi kieu du lieu")
#     except ZeroDivisionError as e:
#         print("Phep chia cho 0")
#     except Exception as e:
#         print("Co loi xay ra vui long thu lai")
#     else:
#         print("a/b = %.2f" % (result))
#     finally:
#         print('Xong')
#         print("---------------------------")
# device(2,6)
# device('a',4)
# device(2,0)
# device(2,'a')
# device(2,'x')

# xử lý nhập dữ liệu
# viết chương trình nhập vào 1 số nguyên, nếu người dùng nhập sai yêu cầu nhập lại tới khi đúng
# while True:
#     try:
#         a = int(input('nhập số nguyên: '))
#     except ValueError as e:
#         print('sai du lieu !!! NHAP LAI')
#     except Exception as e:
#         print('NHAP LAI !!!')
#     else:
#         print('XONG !!!')
#         break
# viết chương trình nhập 2 số để thực hiện phép chia
# nếu nhập sai, gây lỗi thì yêu cầu nhập lại cho tới khi đúng
# thực hiện phép chia
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

#luu y khi su dung try except
#thu tu cua except, can dat cac tinh huong cu the truoc
#tinh huong chung o sau
#else chi chay khi khong co loi
# khoi finally; luon chay du khong co loi
#doc file

# f = open('number.txt', 'w')
# try:
#     data = f.read()
#     print(data)
# except Exception as e:
#     print('co loi xay ra', e)
# finally:
#     f.close()

#phat hien moi loi (chuong trinh, he thong)
# try:
#     print('acv')
# except:
#     print('co loi')
#gom nhieu loi vao 1 khoi lenh
# try:
#     a = int(input('a'))
#     b = a/0
# except (ValueError, ZeroDivisionError) as e:
#     print('co loi xay ra', e)
# try except co the long nhau
# khong nen gom qua nhieu cau lenh logic, xu ly khac nhau trong 1 khoi lenh
# while True:
#     try:
#         a = int(input('a'))
#         b = int(input('b'))
#     except ValueError as e:
#         print('co loi xay ra', e)
#     else:
#         try:
#             print('a/b=', a/b)
#         except Exception as e:
#             print('co loi xay ra', e)
#         else:
#             print('done')
# while True:
#     try:
#         list1 = list(input('nhập số nguyên: '))
#         print(list1)
#         for i in list1:
#             a = int(i)
#             if len(list1) != 5 or isinstance(a, str):
#                 raise Exception
#     except Exception:
#         print('nhập lại')
#     else:
#         while True:
#             try:
#                 b = int(input('nhập vị trí muốn truy xuất: '))
#                 print(f'tại index {b} giá trị =', list1[b])
#             except IndexError as x:
#                 print('vị trí truy xuất không hợp lệ - ', x)
#             except ValueError as y:
#                 print('vị trí truy xuất là số không phải chữ - ', y)
#             else:
#                 print('done')
#                 break
#         break



