"""
Write a python program to store first year percentage of students in an array.                   
Write function for sorting array of floating point numbers in ascending order using:
a) Selection Sort b) Bubble Sort and display top five scores 
"""

A=[]
B=[]
def Accept(A):
	n=int(input("Enter the Total Number of Student:"))
	print("Enter the Marks:")
	for i in range(n):
		x=float(input())
		A.append(x)

def display(A):
	n=len(A)
	if (n==0):
		print("Student Data is Empty")
	else:
		print("Marks are:")
		for i in range(n):
			print(" %.2f"%A[i],end=" ")
		print("\n")

def Selection(A):
	n=len(A)
	for i in range(n):
		minimum=i
		for j in range(i+1,n):
			if(A[minimum]>A[j]):
				minimum=j
		print(A)
		temp=A[i]
		A[i]=A[minimum]
		A[minimum]=temp
	

def Bubble(B):
	n=len(B)
	for i in range(1,n):
		for j in range(n-i):
			if (B[j]>B[j+1]):
				temp=B[j]
				B[j]=B[j+1]
				B[j+1]=temp
		print(B)


main=1
while main:
	print("\n***********MENU***************")
	print("0. Exit")
	print("1. Selection Sort ")
	print("2. Bubble Sort and Top 5 marks")
	print("******************************")
	
	ch=int(input("Enter the Choice:"))
	
	if ch==1:
		Accept(A)
		display(A)
		print("After Selection Sort")
		Selection(A)
		display(A)
	
	elif ch==2:
		Accept(B)
		display(B)
		print("After Bubble Sort")
		Bubble(B)
		display(B)
		n=len(B)
		print("Top 5 Marks:")
		if (n >= 5):
			for i in range(n-1,n-6,-1):
				print("%.2f"%B[i],end=" ")
		else:
			for i in range(n-1,-1,-1):
				print("%.2f"%B[i],end=" ")
	
	elif ch==0:
		main=0
	
	else:
		print("Enter valid choice")


"""
OUTPUT

***********MENU***************
0. Exit
1. Selection Sort
2. Bubble Sort and Top 5 marks
******************************
Enter the Choice:1
Enter the Total Number of Student:5
Enter the Marks:
76
55
46
87
56
Marks are:
 76.00  55.00  46.00  87.00  56.00

After Selection Sort
[76.0, 55.0, 46.0, 87.0, 56.0]
[46.0, 55.0, 76.0, 87.0, 56.0]
[46.0, 55.0, 76.0, 87.0, 56.0]
[46.0, 55.0, 56.0, 87.0, 76.0]
[46.0, 55.0, 56.0, 76.0, 87.0]
Marks are:
 46.00  55.00  56.00  76.00  87.00


***********MENU***************
0. Exit
1. Selection Sort
2. Bubble Sort and Top 5 marks
******************************
Enter the Choice:2
Enter the Total Number of Student:5
Enter the Marks:
45
66
33
78
66
Marks are:
 45.00  66.00  33.00  78.00  66.00

After Bubble Sort
[45.0, 33.0, 66.0, 66.0, 78.0]
[33.0, 45.0, 66.0, 66.0, 78.0]
[33.0, 45.0, 66.0, 66.0, 78.0]
[33.0, 45.0, 66.0, 66.0, 78.0]
Marks are:
 33.00  45.00  66.00  66.00  78.00

Top 5 Marks:
78.00 66.00 66.00 45.00 33.00
***********MENU***************
0. Exit
1. Selection Sort
2. Bubble Sort and Top 5 marks
******************************
Enter the Choice:0
"""