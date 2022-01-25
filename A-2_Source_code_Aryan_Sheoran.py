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

N_1=int(input("Enter first number : "))
N_2=int(input("Enter second number : "))
N_3=int(input("Enter third number : "))
print("\n")
#Finding the greatest number from iput
if N_1>N_2 and N_1>N_3 :
   print("The greatest  number - ",N_1)
elif N_2>N_3:
    print("The greatest  number - ",N_2)
else:
    print("The greatest  number - ",N_3,)
print("\n")    

#Question-5
print("Question-5")
String=str(input("Enter the string : "))
#Providing output depending upon if 'name' is or is not present in string
if "name" in String:
    print("Yes")
else:
    print("No")
print("\n")

#Question-6
print("Question-6")
S_1=int(input("Enter the length of first side : "))
S_2=int(input("Enter the length of second side : "))
S_3=int(input("Enter the length of third side : "))
#Providing output 'Yes' or 'No' depending upon if Triangle is possible or not from input provided by the user.
if S_1>S_2+S_3:
    print("No")
elif S_2>S_1+S_3:
    print("No")
elif S_3>S_1+S_2:
    print("No")
else:
    print("Yes")
