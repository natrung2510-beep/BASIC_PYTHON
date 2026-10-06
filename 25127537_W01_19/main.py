def Bai01():
    myName = "Nguyen Anh Trung"
    print("Hello, world!")
    print(f"My name is {myName}")
    
def Bai02():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    height = float(input("Enter height: "))
    
    print(f"Tên: {name}")
    print(f"Tuổi: {age}")
    print(f"Chiều cao: {height} m")
    
def Bai03():
    s = input("Enter string: ")
    print(len(s))
    print(s.upper())
    print(s.lower())
    print(s[::-1])
    # print("".join(reversed(s)))
    
def Bai04():
    s = "PythonProgramming"
    s1 = s[:6] # Lấy 6 kí tự đầu tiên s[0:6]
    s2 = s[-8:]
    s3 = s1 + s2 
    print(s3)
    
def Bai05():
    nations = ["Việt Nam", "Mỹ", "Ấn Độ", "Trung Quốc", "Lào"]
    print(nations[2])
    nations.append("Campuchia")
    nations[1] = "Thái Lan"
    del nations[0]
    print(nations)
    
def Bai06():
    #tên, tuổi, nghề nghiệp, thành phố.
    person = ("Nguyen Anh Trung", 19, "unemployed", "HCM")
    name, age, job, city = person
    print(name)
    print(age)
    print(job)
    print(city)
# Bai01()
# Bai02()
# Bai03()
# Bai04()
# Bai05()
Bai06()