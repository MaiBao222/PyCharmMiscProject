class Patient:
    def __init__(self, name, priority, time):
        self.name = name
        self.priority = priority
        self.time = time
    def __str__(self):
        return (f"ten benh nhan:{self.name} - "
                f"uu tien:{self.priority} - "
                f"thoi gian vao:{self.time}")
    def __repr__(self):
        return f"TEN:{self.name} - UU TIEN:{self.priority} - GIO VAO:{self.time} "
class Hopital:
    khoa = {"tim":[],"phu san":[],"than kinh":[]}
    list_name = []
    def __init__(self):
        self.name = ""
        self.khoa = Hopital.khoa
    def __repr__(self):
        return f"Patient({self.name})"
    def add_patient(self, key, name):
        self.name = name
        if key in self.khoa:
            self.khoa[key].append(self.name)
            print("da them benh nhan")
        elif key not in self.khoa:
            self.khoa[key] = []
            self.khoa[key].append(self.name)
            print("Khoa moi: da them benh nhan")
    def Listing_patients(self):
        print("+++DANH SACH CAC KHOA+++")
        for spec, patients in self.khoa.items():
            print(f"chuyen khoa: {spec}")
            for p in patients:
                print("benh nhan: ",p)
    def Retrieving(self, specializations):
        print("CHUYEN KHOA: ",specializations)
        self.khoa[specializations].sort(key=lambda p: (p.priority, p.time))
        next_patient = self.khoa[specializations].pop(0)
        print(f"Benh nhan dau tien: {next_patient}")
        print(f"Benh nhan tiep theo")
        for nextp in self.khoa[specializations]:
            print(nextp)
        print("-----------------------")
def menu ():
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter your name: ")
            priority = input("Enter your priority: ")
            time = input("Enter your time: ")
            key = input("Enter your specialization: ")
            Hopital().add_patient(key,Patient(name, priority, time))
        elif choice == "2":
            print("2...")
        elif choice == "3":
            print("3...")
        elif choice == "4":
            print("4...")
        elif choice == "5":
            print("5...")
        elif choice == "6":
            print("6...")
        elif choice == "0":
            print("Exit. Bye bye!")
            break
        else:
            print("Invalid choice. Try again.")










h = Hopital()
h.add_patient("than kinh",Patient("bn133",1,4))

h.add_patient("xuong khop",Patient("bn13",2,7))

h.add_patient("than kinh",Patient("bn182",4,0))

h.add_patient("tim",Patient("bn15",1,8))

h.add_patient("phu san",Patient("bn15",3,5))
h.add_patient("phu san",Patient("bn20",0,9))
h.add_patient("phu san",Patient("bn29",2,10))
h.add_patient("phu san",Patient("bn29",2,10))
h.Listing_patients()
h.Retrieving("phu san")
h.Remove_patient()