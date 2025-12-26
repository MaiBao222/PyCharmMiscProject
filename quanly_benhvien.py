# Adding new patients to specializations (Thêm bệnh nhân mới vào chuyên khoa)
# Listing patients in specializations (Liệt kê bệnh nhân trong các chuyên khoa)
# Retrieving the next patient (Lấy bệnh nhân tiếp theo)
# Removing patient by name (Xóa bệnh nhân theo tên)
# Print all patients super-urgent and urgent (In tất cả bệnh nhân super-urgent và urgent)
# Find patients by patient's name (Tìm kiếm bệnh nhân theo tên)

# class Patient
class Patient:
    def __init__(self, name, status):
        self.name = name
        self.status = status
# class specialization
class Specialization:
    def __init__(self):
        self.patients = []
    def add_patient(self, patient):
        if patient.status == 1:
            self.patients.insert(0, patient) # them benh nhan vao hang dau tien danh sach
        else:
            self.patients.append(patient) # them vao binh thuong theo hang
    def get_next_patient(self):
        if self.patients:
            return self.patients.pop(0)
        else: return None
    def a(self):
        print(self.patients)
# class Hospitalsystem
class Hopitalsystem:
    def __init__(self):
        self.specializations = {
            1: Specialization(), # xuong khop
            2: Specialization(), # tim mach
            3: Specialization(), # tieu hoa
        }
    def add_patient(self):
        name = input("Enter your name: ")
        status = input("Enter your status: ")
        spec = int(input("Enter specialization number: "))
        patient = Patient(name, status)
        self.specializations[spec].add_patient(patient)
    def list_patients(self):
        spec = int(input("Enter specialization number: "))
        patients = self.specializations[spec].patients
        if not patients:
            print("There are no patients in this specialization")
        for p in patients:
            print(f"{p.name} - {p.status}")
    def get_next_patient(self):
        spec = int(input("Enter specialization number:(1-3)"))
        patients = self.specializations[spec].get_next_patient()
        if patients:
            print(f"{patients.name} - {patients.status}")
        else:
            print("There are no patients in this specialization")
    def remove_patient(self):
        name = input("Enter your name: ")
        for spec in self.specializations.values():
            for p in spec.patients:
                if p.name == name:
                    spec.patients.remove(p)
                    print("removed patient from specialization")
        print("Not Found")
    def print_urgent_patients(self):
        for spec in self.specializations.values():
            for p in spec.patients:
                if p.status == 1:
                    print(f"{p.name} - {p.status}")
    def find_patients_by_name(self, name):
        for spec in self.specializations.values():
            for p in spec.patients:
                if p.name == name:
                    print(f"{p.name} - {p.status}")
                    return
        print("Not Found")
    def menu (self):
        print("1. Adding new patients to specializations")
        print("2. Listing patients in specializations")
        print("3. Retrieving the next patient")
        print("4. Print all patients super-urgent and urgent")
        print("5. Find patients by patient's name")
        print("0. Exit")
        while True:
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_patient()
                print("Add new patients to specializations")
            elif choice == "2":
                self.list_patients()
            elif choice == "3":
                self.get_next_patient()
            elif choice == "4":
                self.remove_patient()
            elif choice == "5":
                self.print_urgent_patients()
            elif choice == "6":
                self.find_patients_by_name(input("Enter your name: "))
            elif choice == "0":
                print("Exit. Bye bye!")
                break
            else:
                print("Invalid choice. Try again.")
Hopitalsystem().menu()

# he thong quan ly thu vien
# Problem Statement
#
# A library contains many books.
# Each book has a title, author, ISBN, and availability status.
# A member can borrow and return books.
# The system tracks borrow history
# Book: chính (title, author, ISBN, and availability status.) ~ class Book
# member: ~ class member (hỏi thêm)
# borrow: hàm (return)
# history: ~ class ( tuỷ chọn: phức tạp )

# An online shop sells products.
# Each product has a name, price, and quantity in stock.
# A customer can place an order containing multiple products.
# Each order has a total amount and a payment status.


# Problem Statement
# A university offers multiple courses.
# Each course has a course name, course code, and credits.
# A student can enroll in many courses.
# The system keeps track of enrollments.
# A university offers multiple courses.
# # An online shop sells products.
# A bank manages accounts for customers.
# Each account has an account number, balance, and account type.
# A customer can deposit and withdraw money.
# The bank records transactions.

# A bank manages accounts for customers.
# class: account(account number, balance, and account type), customer(name,...), bank()
# def: deposit, withdraw, records


# class: course(ourse name, course code, and credits),  student(), Uni system()
# def: keeps, enroll


# class: Product (name, price, quantity), Custom (), Each order
# def: total amount, order, list quantity in stock
# danh tu
# + danh tu chinh: 1 danh tu ma duoc bổ sung thông tin bởi danh từ khac ~ class
# + phụ: bổ sung thông tin cho danh tu chính: biến, thuộc tính trong class
# dông tu: ham

