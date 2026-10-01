list0 = [] # Empty List
print(list0)
print(len(list0))
# particular value type of list
list1 = [1,3,4,57,888,999,102,333]
print(list1)
print(len(list1))
print(type(list1))
print(id(list1))
# Homogenious type of list
list2 = ["Hello","Python",'DataScience',383,202.2,3+4j]
print(list2)
# Sort this list Ascending order
list3 = [3,1,4,6,8,1,3,88,49,99]
list3.sort()
print(list3)
# If i wanted to sort in descending order then
list4 =  [3,1,4,6,8,1,3,88,49,99]
list4.sort(reverse=True)
print(list4)
# I wanted to Iterate the list
for value in list4:
    print(value)

# Delete duplicate value from the list
print("Before duplicate list ",list4)
result = list(set(list4))
print("After duplicate shorlist ",result)    
# if order is not preserved then what should i do
relut1 = list(dict.fromkeys(list4))
print(relut1)
# Modify your list
list5 = [3,4,5,6,7,8,9,10,11,23]
list5[4] = 77.8
print(list5)
# use of count- in the list how many element
print(list5.count(5))
print(len(list5))
# Slicing the List
# concept - [start:stop]
# other   - [start:stop:step]
list6 = [1,2,3,4,5,6,7,8,9]
print(list6[2:6])
print(list6[:4])
print(list6[4:])
print(list6[::-1])

# Learn insert, append, extend
list7 = [2,5,6,7,8,9]
list7.append(99)
print(list7)
list7.append([22,33,44,55,66])
print(list7)
print(list7.pop(-1))
print(list7.pop(-2))

list7.insert(0,"Hello")
print(list7)
list7.extend([221])
print(list7)
# Remove, delete and del
list7.remove(221)
print(list7)

colors = ["red", "green", "blue", "yellow", "purple"]
del colors[0]
print(colors)
colors.remove("green")
print(colors)
del colors[1:3]
print(colors)

electronic = ["Laptop","Phone"]
mediatype = ["Mike","speaker"]
electronic.append(mediatype)
print(electronic)      