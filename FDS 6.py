"""
write a python program to store second year percentage of student in array.
write function for sorting array of floating point number in ascending order using
1)insertion sort
2)shell sort and display top five score
"""


A=[]
B=[]
def Accept(A):
	n = int(input("Enter the Number of Student: "))
	print("Enter the Marks: ")
	for i in range (n):
		A.append(float(input()))
	print("Marks Accepted Successfully")



def Display(A):
	n=len(A)
	if (n==0):
		print("List is Empty")
	else:
		print("Marks is :")
		for i in range(n):
			print("%.2f"%A[i],end=" ")
		print("\n")

def insertion(A):
	n=len(A)
	for i in range(1,n):
		minimum=A[i]
		j=i-1
		while(j >= 0):
			if (A[j]<=minimum):
				break
			else:
				A[j+1]=A[j]
				j=j-1
		A[j+1]=minimum
		print(A)


def insertion_gap(A,gap,n,s):
	for i in range(s+gap,n,gap):
		minimum=A[i]
		j=i-gap
		while(j >= 0):
			if (A[j]<=minimum):
				break
			else:
				A[j+gap]=A[j]
				j=j-gap
		A[j+gap]=minimum
		


def shell(A):
	n=len(A)
	gap=int(n/2)
	while( gap >0):
		for s in range(n):
			insertion_gap(A,gap,n,s)
		print(A)
		gap=int(gap/2)

main=1
while main:
	print("\n***********MENU***************")
	print("0. Exit")
	print("1. Insertion sort")
	print("2. Shell Sort and Display Top Five Score")
	print("******************************")
	
	ch=int(input("Enter the Choice:"))
	
	if ch==0:
		main=0
		
	elif ch==1:
		Accept(A)
		Display(A)
		print("After Insertion Sort")
		insertion(A)
		Display(A)
	
	elif ch==2:
		Accept(B)
		Display(B)
		print("After Shell Sort")
		shell(B)
		Display(B)
		print("Top 5 Mark :")
		n=len(B)
		if (n>=5):
			for i in range(n-1,n-6,-1):
				print(B[i],end=" ")
		else:
			for i in range(n-1,-1,-1):
				print(B[i],end=" ")
	
	else:
		print("Enter Valid Choice")

"""
OUTPUT

***********MENU***************
0. Exit
1. Insertion sort
2. Shell Sort and Display Top Five Score
******************************
Enter the Choice:1
Enter the Number of Student: 5
Enter the Marks:
34
55
22
32
12
Marks Accepted Successfully
Marks is :
34.00 55.00 22.00 32.00 12.00

After Insertion Sort
[34.0, 55.0, 22.0, 32.0, 12.0]
[22.0, 34.0, 55.0, 32.0, 12.0]
[22.0, 32.0, 34.0, 55.0, 12.0]
[12.0, 22.0, 32.0, 34.0, 55.0]
Marks is :
12.00 22.00 32.00 34.00 55.00


***********MENU***************
0. Exit
1. Insertion sort
2. Shell Sort and Display Top Five Score
******************************
Enter the Choice:2
Enter the Number of Student: 5
Enter the Marks:
22
55
44
33
11
Marks Accepted Successfully
Marks is :
22.00 55.00 44.00 33.00 11.00

After Shell Sort
[11.0, 33.0, 22.0, 55.0, 44.0]
[11.0, 22.0, 33.0, 44.0, 55.0]
Marks is :
11.00 22.00 33.00 44.00 55.00

Top 5 Mark :
55.0 44.0 33.0 22.0 11.0
***********MENU***************
0. Exit
1. Insertion sort
2. Shell Sort and Display Top Five Score
******************************
Enter the Choice:0
"""