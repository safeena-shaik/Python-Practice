#Write a program to accept marks of 6 students and display them in a sorted 
#manner.
Marks = []
f1 = int(input("enter your Marks"))
Marks.append(f1)
f2 = int(input("enter your Marks"))
Marks.append(f2)
f3 = int(input("enter your Marks"))
Marks.append(f3)
f4 = int(input("enter your Marks"))
Marks.append(f4)
f5 = int(input("enter your Marks"))
Marks.append(f5)
f6 = int(input("enter your Marks"))
Marks.append(f6)
Marks.sort() #sort function is used to sort the value in a ascending order
print(Marks)
