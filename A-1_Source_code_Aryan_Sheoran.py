#Answer 1

#Taking Input
d=int(input('Enter first number : '))
e=int(input('Enter second number : '))
f=int(input('Enter third number : '))
#Finding Average
z=(d+e+f)/3
print('Average = ',z )
print("\n")




#Answer 2

Income=int(input('Enter your income = '))
Members=int(input('No of family members = '))

#Finding Total income

TaxableIncome=Income-(Members*3000)
Tax=TaxableIncome*20/100
print('Taxable Income = ',Tax) 
print("\n")




#Question 3

#input from student
SID=int(input('Enter your SID : '))
Name=input('Enter your name : ')
Gender=input('Enter your gender ( F for female or M for male or U for unknown):')
Course=input('Enter your Course : ')
Cgpa=float(input('Enter yout cgpa : '))
#Printing list
Student=[SID,Name,Gender,Course,Cgpa]
print('Student :',Student)
print("\n")



#Question 4

a=int(input('Enter marks of first student :'))
b=int(input('Enter marks of second student :'))
c=int(input('Enter marks of third student :'))
d=int(input('Enter marks of fourth student :'))
e=int(input('Enter marks of fifth student :'))
Marks=[a ,b ,c ,d ,e ]
#sorting a list
Marks.sort()
print(Marks)
print("\n")

#Question 5

Color=['Red','Green','White','Black','Pink','Yellow']
print('Color',Color)
print("\n")

#a) part
Color.pop(3)
print('(a) New Color :',Color)

print("\n")

#b) part
Color.pop(3)
Color.pop(3)
Color.insert(3,'Purple')
print('(b)New Color :',Color)







