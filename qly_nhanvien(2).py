
class Employee:
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
    def __str__(self):
        return f"Name: {self.name} | Salary: {self.salary} | Age: {self.age}"
    def __repr__(self):
        return self.__str__()
class Manager:
    DS = []
    def __init__(self):
        self.id = 99
    def add_employee(self):
        name = input("Enter employee name: ")
        salary = int(input("Enter salary: "))
        age = int(input("Enter age: "))
        self.id = self.id + 1
        e = Employee(name, salary, age)
        dic = {self.id: e}
        Manager.DS.append(dic)
    def list_employee(self):
        print("------DANH SACH NHAN VIEN------")
        for e in Manager.DS:
            print(e)

    def remove_employee_by_age(self):
        print("--------------------------------")
        max_age = int(input("Enter max age of employee: "))
        min_age = int(input("Enter min age of employee: "))
        for e in Manager.DS[:]:
            for a in e.values():
                if a.age > max_age or a.age < min_age:
                    Manager.DS.remove(e)
    def update_salary(self):
        name = input("Enter employee name: ")
        salary = int(input("Enter employee salary: "))
        for e in Manager.DS:
            for a in e.values():
                En = Employee(a.name, a.salary, a.age).name
                if En == name:
                    a.salary = int(salary)
                else:
                    print("Invalid employee name. Try again.")
    def menu(self):
        while True:
            print("________MENU________")
            print("1. Thêm nhân viên mới")
            print("2. Liệt kê các nhân viên hiện có")
            print("3. Xóa nhân viên theo độ tuổi")
            print("4. Cập nhật lương theo tên")
            print("5. Thoat")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                Manager().add_employee()
            elif choice == 2:
                Manager().list_employee()
            elif choice == 3:
                Manager().remove_employee_by_age()
            elif choice == 4:
                Manager().update_salary()
            elif choice == 5:
                print("BYE")
                break
            else:
                print("Invalid choice. Try again.")
Manager().menu()



