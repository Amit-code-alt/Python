number = (1,2,3,4,5)
print(number)
print(type(number))

number1 = (1,)
print(number1)
print("Blank number ",number1)

color = ("Black","Green","white","Blue","Pink")
print(color)
print(color[1])
print(color[0])
print(color[1:4])
print(color[-1])
print(color[:3])
print(color[3:])

python_student = ("Ramesh","Mahesh","Ganesh","Somesh","Jayesh")
print(python_student)
print(python_student[2])
for data in python_student:
    print(data,end="|")
    if data == "Ramesh":
        print("Match Found")       
    else:
        print("Match not Found")



print(len(python_student))

x = (10,10)
print(type(x))


student = ("Alice",24,"Python")
name,age,course = student
print(name)
print(age)
print(course)    

print("==============================")
number = (3,4,5,6,7,8,2,11,11,11)
print(number)
first,*middle,last=number
print(first)
print(middle)
print(last)

a =(3,5)
b =(4,6)
print(a + b)
print(a.count(3))
print(a.count(1))
print(a.index(3))

carts = ("Apple","Lenvo","Dell","HP")
