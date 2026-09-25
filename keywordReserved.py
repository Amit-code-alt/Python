import keyword as kw
print(kw.kwlist)
print("--------------")
print(kw.iskeyword)
print(kw.softkwlist)

numberoption  = int(input("Enter any Number"))
if numberoption == 10:
    print("You have good choice")
else:
    print("Bad Number choice")

# input alway return as a string

other = input("Enter any number")
print(other,other.title())    