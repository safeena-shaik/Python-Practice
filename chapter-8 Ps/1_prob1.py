'''
def greatest():
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    c=int(input("enter the number:"))
    if a>b and a>c:
        print(f"{a} is greater")
    elif b>a and b>c:
         print(f"{b} is greater")
    elif c>a and c>b:
         print(f"{c} is greater")
greatest()
'''
#Another simple method using arguments
a=1
b=2
c=3
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
a=1
b=2
c=3
print(greatest(a,b,c))