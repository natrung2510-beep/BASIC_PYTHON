 
import math
import json

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


def greet(name, age):
    print(f"Xin chào {name}, bạn {age} tuổi.")
def Bai13():
    name = "Trung"
    age = 19
    greet(name, age)

def describe_person(*args, **kwargs):
    print("Sở thích:", args)
    print("Thông tin:", kwargs)
    
def Bai14():
    describe_person("Đá bóng", "Nghe nhạc", name="Trung", age=19, city="HCM")

def factorial(n: int) -> int: 
    if n <= 1 :
        return 1
    
    return n * factorial(n - 1)
def Bai15():
    n = int(input("Enter an integer: "))
    res = factorial(n)
    print(n, "! =", res)

def Bai16():
    x = int(input("Enter an integer: "))
    square_root = math.sqrt(x)
    print(f"sqrt({x})= {square_root}")
    print(f"ceiling sqrt({x})= {math.ceil(square_root)}")
    
def Bai17():
    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")

def Bai18():
    try:
        a = float(input("Nhập số chia: "))
        b = float(input("Nhập số bị chia: "))
    
        res = a / b
        print(f"Kết quả của {a} : {b} là {res}")
    except ValueError:
        print("Lỗi: Dữ liệu nhập vào không phải là số hợp lệ!")
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho số 0!")

def Bai19():
    json_str = '{"name": "Mai", "age": 25, "city": "Hanoi"}'
    # 1. Chuyển chuỗi JSON thành Dictionary bằng json.loads
    person_dict = json.loads(json_str)
    
    print(f'Tên: {person_dict["name"]}')
    print(f'Tuổi: {person_dict["age"]}')
    print(f'Thành phố: {person_dict["city"]}')
    
    new_json_str = json.dumps(person_dict)
    print("Chuỗi JSON sau khi chuyển đổi:", new_json_str)



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
# Bai12()
# Bai13()
# Bai14()
# Bai15()
# Bai16()
# Bai17()
# Bai18()
Bai19()