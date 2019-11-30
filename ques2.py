try:
    n= input("Please enter an integer")
    n = int(n)
except ValueError:
    print("No Valid Integer")


try:
    a=5
    b="cnm"
    c = a+b
except TypeError:
    print("Type Exception Occured")

try:
    a=8
    a.append(4)
except AttributeError:
    print("Attribute Error occured")
