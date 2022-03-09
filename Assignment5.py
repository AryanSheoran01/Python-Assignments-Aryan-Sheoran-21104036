#ANSWER 1 

#GUI-based GST Tax Finder Calculator

#GST rate = ((Net Price - Original Cost) * 100) / Original Cost

#Importing
from tkinter import *

#Using Functions
def Find_GST():
    
    Original_Cost = int(Original_RateField.get())

    Net_Price = int(Net_RateField.get())

    # Calculating GST rate
    GST_Rate = ((Net_Price - Original_Cost) * 100) / Original_Cost

    #Using insert method for inserting the value in the text entry box.
    GST_RateField.insert(10, str(GST_Rate) + " % ")


#Using Function for clearing the contents of all text entry boxes

def clearAll():
    
    Original_RateField.delete(0, END)

    Net_RateField.delete(0, END)

    GST_RateField.delete(0, END)


# Driver Code 
if __name__ == "__main__":

#Creating a GUI window
    gui = Tk()

    #Background
    gui.configure(background="yellow")

    #Naming of tkinter GUI window
    gui.title("GST Tax Finder")

    #Configuration of GUI window
    gui.geometry("400x400")

    #Creating a Original Price : Label
    Original_Price = Label(gui, text="Original Price",
                      bg="orange")

    #Creating a Net Price : Label
    Net_Price = Label(gui, text="Net Price",
                      bg="orange")

    #Creating a Find Button 
    Search_1 = Button(gui, text="Find", fg="Black",
                  bg="Red",
                  command=Find_GST)

    #Creating a Gst Rate : label
    GST_Rate = Label(gui, text="Gst Rate", bg="orange")

    #Creating a Clear Button 
    clear = Button(gui, text="Clear", fg="Black",
                   bg="Red",
                   command=clearAll)

#Using grid method : Used for placing the widgets at respective positions in table like structure.

    Original_Price.grid(row=1, column=1, padx=10, pady=10)

    Net_Price.grid(row=2, column=1, padx=10, pady=10)

    Search_1.grid(row=3, column=2, padx=10, pady=10)

    GST_Rate.grid(row=4, column=1, padx=10, pady=10)

    clear.grid(row=5, column=2, padx=10, pady=10)

#Creating a text entry box for filling or typing the information.
    Original_RateField = Entry(gui)

    Net_RateField = Entry(gui)

    GST_RateField = Entry(gui)

    Original_RateField.grid(row=1, column=2, padx=10, pady=10)

    Net_RateField.grid(row=2, column=2, padx=10, pady=10)

    GST_RateField.grid(row=4, column=2, padx=10, pady=10)

    #Starting GUI
    gui.mainloop()


#ANSWER 2   
# To create a GUI-based Calendar application using Tkinter module

#Importing 
from hashlib import new
from tkinter import *
#Importing calender module
import calendar
from tkinter import font

#Function for showing the calender of the given year
def showCal():
    # Create a GUI window
    New_GUI = Tk()

    #Background Colour
    New_GUI.config(background= "white")
   
    New_GUI.title("CALENDAR")

    #Configuration
    New_GUI.geometry("500x600")

    
    Fetch_Year = int(Year_Field.get())


    #The calendar of the given year 
    Calender_Content = calendar.calendar(Fetch_Year)

    #Creating label for showing the content of the calendar
    Calender_Year = Label(New_GUI, text= Calender_Content, font="Consolas 10 bold")

    #Using Grid method is used for placing 
    
    Calender_Year.grid(row= 5, column= 1, padx= 20)

    #Starting GUI
    New_GUI.mainloop()

# Driver Code for this question
if __name__ == "__main__":
    # Create a GUI window
    gui = Tk()

    #Background colour
    gui.config(background= "white")

    #Naming tkinter GUI window
    gui.title("CALENDAR")

    #Configuration of GUI window
    gui.geometry("300x180")

    #Creating a CALENDAR : Label with specified font and size 
    cal = Label(gui, text= "CALENDAR", bg= "pink", font= ("times", 22 , "bold"))

    #Creating Enter Year : Label
    year = Label(gui, text= "Enter Year", bg= "orange")

    #Creating text entry box for filling or typing the information
    Year_Field = Entry(gui)

    #Creating a calendar button
    Show = Button(gui, text= "Show Calender", fg="Black", bg="light green", command= showCal) 

    #Creating a Exit button 
    Exit = Button(gui, text= "Exit", fg= "Black", bg= "light green", command= exit)

    #Using grid method :used for placing the widgets at respective positions in table like structure
    cal.grid(row= 1, column= 1)
    year.grid(row= 2, column= 1)
    Year_Field.grid(row= 3, column= 1)
    Show.grid(row= 4, column= 1)
    Exit.grid(row= 6, column= 1)

#Starting  GUI
    gui.mainloop()



#Answer3

# Question ---> 3
# To create a GUI-based calculator using Tkinter module
# It performs operations like addition, subtraction, multiplication, and division

from ast import Lambda
import math
from tkinter import *

root = Tk()

Calculator_GUI = Entry(root, width=35, borderwidth=5)
Calculator_GUI.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Calculator_GUI.insert(0, "Enter your name : ")

def button_click(number):
    # Calculator_GUI.delete(0, END)
    current = Calculator_GUI.get()
    Calculator_GUI.delete(0, END)
    Calculator_GUI.insert(0, str(current) + str(number))

def button_clear():
    Calculator_GUI.delete(0, END)

def button_add():
    first_number = Calculator_GUI.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    Calculator_GUI.delete(0, END)

def button_equal():
    second_number = Calculator_GUI.get()
    Calculator_GUI.delete(0, END)

    if math == "addition":
        Calculator_GUI.insert(0, f_num + int(second_number))

    if math == "subtraction":
        Calculator_GUI.insert(0, f_num - int(second_number))

    if math == "multiplication":
        Calculator_GUI.insert(0, f_num * int(second_number))

    if math == "division":
        Calculator_GUI.insert(0, f_num / int(second_number))


def button_subtract():
    first_number = Calculator_GUI.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    Calculator_GUI.delete(0, END)



def button_multiply():
    first_number = Calculator_GUI.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    Calculator_GUI.delete(0, END)


def button_divide():
    first_number = Calculator_GUI.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    Calculator_GUI.delete(0, END)


#Defining Buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command= button_add)
button_equal = Button(root, text="=", padx=101, pady=20, command= button_equal)
button_clear = Button(root, text="Clear", padx=90, pady=20, command= button_clear)

button_subtract = Button(root, text="-", padx=40, pady=20, command= button_subtract)
button_multiply = Button(root, text="*", padx=41, pady=20, command= button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command= button_divide)
# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)


root.mainloop()



#QUESTION4
print("ANSWER 4")
def partition(arr, low, high):
	i = (low-1)		 # index of smaller element
	pivot = arr[high]	 # pivot

	for j in range(low, high):

		# If current element is smaller than or
		# equal to pivot
		if arr[j] <= pivot:

			# increment index of smaller element
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort


def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:

		# pi is partitioning index, arr[p] is now
		# at right place
		pi = partition(arr, low, high)

		# Separately sort elements before
		# partition and after partition
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)


# Driver code to test above  
arr = [23 ,12 , 33, 34]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
	print("%d" % arr[i])
#Answer 5
print("Answer 5 \n")                                         
List_Array=list(map(int,input(" Please Enter space separated integers:").split()))

#Defining sorting functions

def bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]

#Printing sorted input
bubble_sort(List_Array)
print(f"\n(A)\n Sorting the input Array: {List_Array}")

#B part
print("\n(B)")
#Defining binary search
def binary_search(list,search,l,u):
    global i
    m=(l+u)//2
    m_element=list[m]
    while l<=u:
        m = (l + u) // 2
        m_element = list[m]
        if m_element==search:
            return [True,list.index(search)]
        else:
            if m_element<search:
                l=m+1
            elif m_element>search:
                u=m-1
    return False,"random"

#Taking input of Integer to Find
Search_1=int(input("Enter number to search in list:"))

if binary_search(List_Array,Search_1,0,len(List_Array)-1)[0]:
    print(f"The integer {Search_1} is present at Index "
          f"{binary_search(List_Array,Search_1,0,len(List_Array)-1)[1]} in the list {List_Array}")
else:
    print(f"Error\nInteger {Search_1} is not present in the list")

#Part C
print("\n(C)\n")
count=0
for e in List_Array:
    if e==Search_1:
        count=count+1
print(f"Number of occurrences of {Search_1} in the list is:{count}")