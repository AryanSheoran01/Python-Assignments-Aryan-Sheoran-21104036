#ANSWER 1

print("\n ANSWER 1 \n")

#Defining Tower of Hanoi

def Hanoi_Tower(n , from_rod, to_rod, middle_rod):
	if n == 0:
		return
	Hanoi_Tower(n-1, from_rod, middle_rod, to_rod)
	print("Move disk",n,"from rod",from_rod,"to rod",to_rod)

#Using the function of tower of hanoi    

	Hanoi_Tower(n-1, middle_rod, to_rod, from_rod)
n = 3
Hanoi_Tower(n, 'A', 'C', 'B')



#ANSWER 2
print("\n ANSWER 2 \n")

#IMPORTING
from math import factorial, remainder
from tracemalloc import start
Size_Triangle=int(input("Enter the size of Pascal's triangle "))

#ITERATIVE PROCEDURE
print("ITERATIVE PROCEDURE")
print("Using 'WHILE' Loop")

i=0
while(i<Size_Triangle):
    z=Size_Triangle-i+1
    while(z>0):
        print(end=" ")
        z-=1
    y=0
    while(y<i+1):
        print(factorial(i) // (factorial(y) * factorial(i - y)), end=" ")
        y+=1
    i+=1
    print()
print("\n\n")

#USING RECURSSIONS

print("USING RECURSSIONS")
def Pascal_Triangle(Size_Triangle,Original_Length=Size_Triangle):
    if Size_Triangle == 0:
        return
    Pascal_Triangle(Size_Triangle-1,Original_Length)
    
    print('  '*(Original_Length-Size_Triangle), end='')

    start = 1
    for i in range(1, Size_Triangle+1):

        print(start, end ='   ')

#USING BINOMIAL COEFFICIENT FOR PASCALS TRIANGLE        
        
        start = start * (Size_Triangle - i) // i
    print()
Pascal_Triangle(Size_Triangle)


#ANSWER 3
print("\n ANSWER 3 \n")

I_1, I_2 = map(int,input("Enter two numbers : ").split())
Quotient = I_1 // I_2
Remainder = I_1 % I_2
print("Quotient :",Quotient)
print("Remainder :",Remainder)
#A PART
print("(A) Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))

#B PART
if (Quotient == 0):
    print("(B) The quotient is zero")
if (Remainder == 0):
    print("(B) The reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print("(B) All the values are non zero")

#C PART
LIST_1 = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(LIST_1)):
    if LIST_1[i] > 4:
        result.append(LIST_1[i])       
print(f"(C) Filtered out numbers that are greater than 4 are : {result}")

#D PART
SET_RESULT = set(result)
print("(D) Set:",SET_RESULT)

#E PART
IMMUTABLE_SET = frozenset(SET_RESULT) #frozen Set is used to make the set immutable
print("(E)Immutable set:",IMMUTABLE_SET)

#F PART
print("(F) Hash value of the max value from the above set:", hash(max(IMMUTABLE_SET)))


#ANSWER 4
print("\n ANSWER 4 \n")
class Student:
    def __init__(self, student,roll_no):
        self.name = student
        self.roll_no = roll_no
    
    def __del__(self):
        print("Object destroyed")

Student_1 = Student("Aryan Sheoran", 21104036)
print("Object created")

print("The name of the student is",Student_1.name," and SID is", Student_1.roll_no)

del Student_1



#ANSWER 5
print("\n ANSWER 5 \n")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
#Creating employee records
Employee_1 = Employee("Mehak", 40000)
Employee_2 = Employee("Ashok", 50000)
Employee_3 = Employee("Viren", 60000)

#A part
#Updating salary
Employee_1.salary = 70000
print("(A) The updated salary of",Employee_1.name,"is",Employee_1.salary)

#B part
#Deleting record
print("(B) Record of Varun deleted", end='')
del Employee_3



#Answer 6
print("\n ANSWER 6 \n")
#Inputting a word from Greoge
Word_1 =input("Enter the word: \n")
Word_1=Word_1.lower()

#Entering meamimg full word from same letters
Test_Word = input("Enter a new meaningful word using the exact same letters to test your friendship: \n")
Test_Word=Test_Word.lower()

#Using Dictionary
def count_in_dict(word):
    count = {}
    List_1 = list(word)
    
    n = len(List_1)
    for i in range(n):
        if List_1[i] in count:
            count[List_1[i]] += 1
        else:
            count[List_1[i]] = 1
    return count

def userinput():
    if count_in_dict(Word_1) != count_in_dict(Test_Word):
        print("Your friendship is fake")
        return
    Answer_1 = input("Does the word makes sense?(y/Y or n/N )")

    if Answer_1 == 'y' or Answer_1=='Y':
        print("Your Friendship is true")
    elif Answer_1 == 'n' or Answer_1=='N':
        print("The word doesn't have a meaning, friendship is fake")
    else:
        print("Invalid input,try again with y/Y or n/N ")
        userinput()
userinput()
