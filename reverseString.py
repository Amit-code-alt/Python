def reversedSimpleString(str):
    temstr = " "
    for i in str:
        temstr = i + temstr
    return temstr


orgn = "HELLO"
print("Original Value is ", orgn)
print("After Reversed   ", reversedSimpleString(orgn))

#----------------------------------

def reversed(original):
    tem = original[::-1]
    return tem

print("Reversed String ", reversed("FIRST"))       