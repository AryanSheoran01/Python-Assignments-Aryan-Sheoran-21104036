#Question1
print("Answer:1 \n")

String=str(input("Enter a word or line :\n"))
#CONVERTING USER INPUT INTO LOWER CASE    
String=String.lower()   
Length_String=len(String) 

#COVERT 'String' INTO LIST
Split_String=String.split()

#CALCULATING NO OF ELEMENTS IN GROUP
Length_of_Split_String=len(Split_String) 

#IF STRING=ONE WORD
if Length_of_Split_String==1:
    dict1={}  
    for x in range(0,Length_String):
        dict1.update({String[x]:String.count(String[x])})
    print("Calculating number of Occurrences of each character as the single word is entered by the user :\n",dict1)    
    
#IF STRING=MORE THAN ONE WORD
elif Length_of_Split_String>1:
    dict={}
    for y in range(0,Length_of_Split_String):
        dict.update({Split_String[y]:Split_String.count(Split_String[y])})
    print("Calculating Number of Occurrences of each word in line entered by the user:\n",dict)   

else :
    print("Enter a word or line \n")







#Question2
print("\n Answer 2")

Year =int(input("Please Enter Year: "))  

#Checking whether user input is a leap year or not

if Year%4==0:
    Leap_year=True
else:
    Leap_year=False


if Year in range(1800,2025):
    Month=int(input("Please Enter Month: ")) 
    #Months having 30 Days
    if Month in (4,6,9,11):      
        Day=int(input("Enter Day: "))
        if Day in range(1,30):
            print(F"Next Date in the format(dd/mm/yyyy) is: {Day+1}/{Month}/{Year} ")
            
        elif Day==30:
            print(F"Next Date in the format(dd/mm/yyyy) is: {1}/{Month+1}/{Year} ")
            
        else:
            print("Error:Please Provide a valid day (1-30 for this month)")

    #Month having 31 days
    elif Month in (1,3,5,7,8,10):  
        Day=int(input("Please Enter Day: "))
        if Day in range(1,31):
            print(F"Next date in the format(dd/mm/yyyy) is: {Day+1}/{Month}/{Year} ")
        elif Day==31:
            print(F"Next date in the format(dd/mm/yyyy) is: {1}/{Month+1}/{Year} ")
            
        else:
            print("Error:Please provide a valid day (1-31 for this month)")

    #Considering December as separate
    elif Month==12:  
        Day=int(input("Please Enter day: "))
        if Day in range(1,31):
            print(f"Next date in the format(dd/mm/yyyy) is: {Day+1}/{Month}/{Year} ")
            
        elif Day==31:
            print(f"Next date in the format(dd/mm/yyyy) is: {1}/{1}/{Year+1} ")
            
        else:
            print("Error: Please provide a valid day (1-31 for this month)")

    #February
    elif Month==2: 
        #If user entered year is leapyear 
        if Leap_year==True:   
            Day=int(input("Please Enter Day: "))
            if Day in range(1,29):
                print(F"Next date in the format(dd/mm/yyyy) is: {Day+1}/{Month}/{Year} ")
                
            elif Day==29:
                print(F"Next date in the format(dd/mm/yyyy) is: {1}/{Month+1}/{Year} ")
                
            else:
                print("Error: Please Enter a valid day (1-29 for this month)")
        
        #If User entered year is non-leap year
        elif Leap_year==False:  
            Day=int(input("Please Enter day: "))
            if Day in range(1,28):
                print(F"Next date in the format(dd/mm/yyyy) is: {Day+1}/{Month}/{Year} ")
                
            elif Day==28:
                print(f"Next date in the format(dd/mm/yyyy) is: {1}/{Month+1}/{Year} ")
                
            else:
                print("Error: Please Enter a valid day (1-28 for this month)")
            
    else:
        print("Error:Please Enter Valid month (1-12) ")

else:
    print("Error:Please Enter Valid Year Between (1800-2025)")





#Question3
print("\n Answer : 3") 


Count_Items_List=int(input("Please provide number of items to be added:\n"))    

List1=[] 
for i in range(1,Count_Items_List+1):
     Items_List=int(input(F"Please enter item(number): \n"))  
     List1.append(Items_List)

#Creating a list of tuples with the first element as the number and Second element as the square of the number
New_List=[]   
i=0
for i in range (0,Count_Items_List):  
     New_List.append((List1[i], List1[i]**2))
     i=i+1

print("\nRequired list is :\n",New_List)




#Question 4
print("\nAnswer : 4\n")

Grade_point=int(input("Your grade point: "))  

#Providing output as per user's input grade point
if 4<=Grade_point<=10:
    if Grade_point==10:
        Grade="A+"
        Performance="Outstanding"

    elif Grade_point==9:
        Grade="A"
        Performance="Excellent"

    elif Grade_point==8:
        Grade="B+"
        Performance="Very Good"

    elif Grade_point==7:
        Grade="B"
        Performance="Good"

    elif Grade_point==6:
        Grade="C+"
        Performance="Average"

    elif Grade_point==5:
        Grade="C"
        Performance="Below Average"

    elif Grade_point==4:
        Grade="D"
        Performance="Poor"

    print(F"Your grade is '{Grade}' and {Performance} performance")

else:
    print("ERROR (Grade point should be in range 4-10)")





#Question 5

print("\n Answer : 5 ")

Pattern='ABCDEFGHIJK'   
#Removing last two letters from Pattern with each loop
for i in range(0,6):
    print(' '*i,Pattern[0:(11-(i*2))])



#Question 6
print("\nAnswer : 6")


Dict_1={}  
#Making 1st entry as default      
i="y"          
if i=="y" :

    #Repeatedly asking user to enter name and SID using while loop

    while i=="y" or i=="Y":              
        Student_Name=str(input("\nEnter name: "))  
        Student_SID=int(input("Enter SID: "))      
        if Student_SID<=0:
            print("ERROR: SID SHOULD BE POSITIVE ")
            exit()
        Dict_1.update({Student_Name:Student_SID})               
        print(Dict_1)

        #Asking User to enter more inputs in Dict_1
        i=input("\nWant to Add more entry?\nPress 'Y' for YES / 'N' for NO.\n")    
                                        
  
    if i=="n" or i=="N":                 
        
        #a)
        print("\n a) The Required dictionary is\n",Dict_1)  
        
       
       
        #part b)
        List_1=Dict_1.keys() 
        #Sorting list on the basis of names              
        sorted_List_1=sorted(List_1)     
       
        Dict_2={}                    
        for items in sorted_List_1:
            Dict_2.update({items:Dict_1.get(items)})

        print("\nb) Dictionary sorted on the basis of names:\n",Dict_2)
        

        
        # part c)
        #Making a new dict with SIDs as keys and name as values
        Dict_3={}                     
        for key,value in Dict_1.items():
            Dict_3.update({value:key})

        List_2=Dict_3.keys()
        #Sorting list on the basis of SIDS          
        Sorted_list_2=sorted(List_2)    
        
        #Making a new dictionary sorted on  the basis of SIDs
        Dict_4={}                    
        for items in Sorted_list_2:
            Dict_4.update({Dict_3.get(items):items})

        print("\nc) Dictionary sorted on the basis of SID:\n",Dict_4)

        

        #part d)
        #Taking SID as input to print the name assigned with it
        SID=int(input("\nd) Enter a SID to get it's name:"))  
        if SID in List_2:
            print("Name related to following sid is:\n",Dict_3.get(SID))
        else:
            print("ERROR: The following SID is not present in dictionary")

   
    else:
        print("ERROR : Enter 'Y' or 'N' only" )




# Question 7
print("\nAnswer: 7\n")


Number_Terms=int(input("How many terms are to be printed in fibonacci series?\n"))  

N_1=0   
N_2=1

if Number_Terms<=0:
    print("ERROR:ENTER POSITIVE ONLY")

else:
    List_1=[]   
    for i in range (0,Number_Terms-1):
        if i==0:
            #Entering '0' as first term in List_1
            List_1.append(N_1)    
        if i==1:
            #Entering '1' as second term in List_1
            List_1.append(N_2)    
            continue
        sum=N_1+N_2
        N_1=N_2
        N_2=sum
        List_1.append(sum)     
        sum+=sum

    print("\nRequired Fibonacci series is:\n",List_1)

    
    #Calculating sum 
    sum=0
    for items in List_1:
        sum=sum+items
    #Calculating average
    Average=sum/len(List_1)  
    print("\nAverage of following series is:\n",Average)








#QUESION 8
print("\nAnswer: 8\n")
#Given
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

#a)
print("a)", end=" ")
a=(set1^set2)  
print(a)


#b)
print("b)", end=" ")
b=(set1^set2^set3)  
print(b)

#c)
print("c)", end=" ")
print((set1|set2|set3)-(set1^set2^set3)-(set1&set2&set3))  
   

#d)
print("d)", end=" ")
I_1={1,2,3,4,5,6,7,8,9,10}
print(I_1-set1)

#e)
print("e)", end=" ")
print(I_1-(set1|set2|set3))   

















