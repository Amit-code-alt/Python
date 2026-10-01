number = {1,2,3,4,5,6,7,8,4,5,6,7}
print(type(number))
print(number)

number.add(99)
print(number)
number.add(1)
print(number)
for item in number:
    print(item,end="|")

python_student = {"Mike","Joye","Takos","Sadar"}
java_Student ={"Amit","Kumar","Mike"}
combinedstudent = python_student | java_Student
print(combinedstudent)

python_student.union(java_Student)
print(python_student)

print(python_student & java_Student)
print(python_student or java_Student)

print(python_student - java_Student)

# Square the number

stset = {1,2,3,4,1,2,3,4}

square = {x * 2 for x in stset}
print(square)

print("count of the set length ",len(stset))
print(stset(range(1,7)))