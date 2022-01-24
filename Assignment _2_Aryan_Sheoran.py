#Question-1
print("Question-1")
Text="Python is a case sensitive language"
#a)
print("a) Length =" , len(Text) ,"\n")
#b)
print("b)",Text[::-1],"\n")
#c)
print("c)", Text[10:26] , "\n")
#d)
print("d)",Text.replace("a case sensitive","object oriented"),"\n")
#e)
print("e)", Text.find("a"),"\n")
#f)
print("f)",Text.replace(" ",""),"\n")

#Question-2
print("Question-2")
name=input("Enter your name - ")
Id=input("Enter your SID - ")
Branch=input("Enter your department - ")
Cgpa=input("Enter your CGPA - ")
print("\n")
print("Hey,", name,"Here!")
print("My SID is",Id)
print("I am from",Branch,"department","and my CGPA is",Cgpa,"\n")

#Question-3
print("Question-3")
#      32 16 8 4 2 1
#a=56   1  1 1 0 0 0
#b=10   0  0 1 0 1 0
a=56
b=10
print("a&b is:",a&b,"\n")
print("a|b is:",a|b,"\n")
print("a^b is:",a^b,"\n")
print("a<<2:",a<<2,"  ","b<<2:",b<<2,"\n")
print("a>>2:",a>>2,"   ","b>>4:",b>>4,"\n")

#Question-4
print("Question-4")

a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))
print("\n")
if a>b and a>c :
   print("The greatest  number - ",a)
elif b>c:
    print("The greatest  number - ",b)
else:
    print("The greatest  number - ",c,)
print("\n")    

#Question-5
print("Question-5")
a=str(input("Enter the string : "))
if "name" in a:
    print("Yes")
else:
    print("No")
print("\n")

#Question-6
print("Question-6")
a=int(input("Enter the length of first side : "))
b=int(input("Enter the length of second side : "))
c=int(input("Enter the length of third side : "))
if a>b+c:
    print("No")
elif b>a+c:
    print("No")
elif c>a+b:
    print("No")
else:
    print("Yes")
