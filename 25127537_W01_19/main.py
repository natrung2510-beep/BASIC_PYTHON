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
    
def Bai07():
    ls = [1, 2, 2, 3, 4, 4, 5]
    s = set(ls)
    s.add(6)
    print(s)
    
def Bai08():
    student = {
    "name": "An",
    "age": 21,
    "major": "Computer Science",
    }
    
    print(student["name"])
    student["age"] = 22
    student.update({"GPA": 3.5})
    del student["major"]
    print(student)
    
def Bai09():
    n = int(input("Enter an integer: "))
    
    if n > 0:
        print("Số dương")
    elif n < 0:
        print("Số âm")
    else: 
        print("Số không")
        
def Bai10():
    for i in range(1,11):
        print(i)
        
    for j in range(1,11):
        if j % 2 == 0:
            print(j)
            
def Bai11():
    n = int(input("Enter an integer: "))
    i = 1
    sum = 0
    while i <= n:
        sum += i
        i += 1
    print(sum)

def Bai12():
    ls = [1,2,3,4,5,6,7,8,9,10]
    # squares = []
    # for x in range(1, 11):
    #     squares.append(x**2)
    
    # [biểu_thức for phần_tử in tập_hợp]
    evens = []
    for i in ls:
        if i % 2 == 0:
            evens.append(i)
            
    squares = [x**2 for x in evens]
    print(squares)


def Bai13():
    print()

def Bai14():
    print()

def Bai15():
    print()

def Bai16():
    print()
    
def Bai17():
    print()

def Bai18():
    print()

def Bai19():
    print()



# Bai01()
# Bai02()
# Bai03()
# Bai04()
# Bai05()
# Bai06()
# Bai07()
# Bai08()
# Bai09()
# Bai10()
# Bai11()
Bai12()
# Bai13()
# Bai14()
# Bai15()
# Bai16()
# Bai17()
# Bai18()
# Bai19()