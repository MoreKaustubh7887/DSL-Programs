"""
Write a Python program to compute following computation on matrix:
a) Addition of two matrices B) Subtraction of two matrices
c) Multiplication of two matrices d) Transpose of a matrix
"""

M1=[]
M2=[]
M3=[] 
M4=[]
M5=[]

def Accept(M):
	r=int(input("Enter the Number of Row:"))
	c=int(input("Enter the Number of Column:"))
	
	print("Enter the element of Matrix:")
	for i in range(r):
		A=[]
		for j in range(c):
			A.append(int(input()))
		M.append(A)

def Display(M,r,c):
	for i in range(r):
		for j in range(c):
			print(M[i][j],end=" ")
		print()

def Add(M1,M2,M3,r,c):
	for i in range(r):
		A=[]
		for j in range(c):
			A.append(M1[i][j] + M2[i][j])
		M3.append(A)
	
	
def Sub(M1,M2,M4,r,c):
	for i in range(r):
		B=[]
		for j in range(c):
			B.append(M1[i][j] - M2[i][j])
		M4.append(B)
	
def Mul(M1,M2,M5,r1,c1,c2):
	for i in range(r1):
		C=[]
		for j in range(c1):
			Sum=0
			for k in range(c2):
				Sum=Sum + (M1[i][k] * M2[k][j])
			C.append(Sum)
		M5.append(C)

def trans(M,r,c):
	for i in range(r):
		D=[]
		for j in range(c):
			print(M[j][i],end=" ")
		print()
			


main=1
while main:
	print("**********MENU***************")
	print("0. Exit")
	print("1. Accept Matrix")
	print("2. Display Matrix")
	print("3. Sum of Matrix")
	print("4. Subtraction of matrix")
	print("5. Multiplication of Matrix")
	print("6. Transpose of Matrix")
	print("*****************************")
	
	ch=int(input("enter the choice:"))
	
	if ch==1:
		print("\n First Matrix:")
		Accept(M1)
		r1 = len(M1)
		c1 = len(M1[0])
		print("\n Second Matrix:")
		Accept(M2)
		r2 = len(M2)
		c2 = len(M2[0])
		
	elif ch==2:
		print("\nFirst Matrix is:")
		Display(M1,r1,c1)
		print("\nSecond Matrix is:")
		Display(M2,r2,c2)
		
	elif ch==3:
		if(r1==r2 and c1==c2):
			Add(M1,M2,M3,r1,c1)
			print("Addition is:")
			Display(M3,r1,c1)
		else:
			print("Addition Not Possible")
		
	elif ch==4:
		if(r1==r2 and c1==c2):
			Sub(M1,M2,M4,r1,c1)
			print("Subtraction is:")
			Display(M4,r1,c1)
		else:
			print("Subtraction Not Possible")
	
	elif ch==5:
		if(c1 == r2):
			Mul(M1,M2,M5,r1,c1,c2)
			print("Multiplication is:")
			Display(M5,r1,c2)
		else:
			print("Multiplication Not Possible")
		
	elif ch==6:
		print("\nTranspose of First Matrix")
		trans(M1,r1,c1)
		print("\nTranspose of Second Matrix")
		trans(M2,r2,c2)
	
	elif ch==0:
		main=0
	
	else :
		print("Enter Valid Choice")
		

"""
OUTPUT
**********MENU***************
0. Exit
1. Accept Matrix
2. Display Matrix
3. Sum of Matrix
4. Subtraction of matrix
5. Multiplication of Matrix
6. Transpose of Matrix
*****************************
enter the choice:1

 First Matrix:
Enter the Number of Row:2
Enter the Number of Column:2
Enter the element of Matrix:
1
2
3
4

 Second Matrix:
Enter the Number of Row:2
Enter the Number of Column:2
Enter the element of Matrix:
1
2
3
4
**********MENU***************
0. Exit
1. Accept Matrix
2. Display Matrix
3. Sum of Matrix
4. Subtraction of matrix
5. Multiplication of Matrix
6. Transpose of Matrix
*****************************
enter the choice:2

First Matrix is:
1 2
3 4

Second Matrix is:
1 2
3 4
**********MENU***************
0. Exit
1. Accept Matrix
2. Display Matrix
3. Sum of Matrix
4. Subtraction of matrix
5. Multiplication of Matrix
6. Transpose of Matrix
*****************************
enter the choice:3
Addition is:
2 4
6 8
**********MENU***************
0. Exit
1. Accept Matrix
2. Display Matrix
3. Sum of Matrix
4. Subtraction of matrix
5. Multiplication of Matrix
6. Transpose of Matrix
*****************************
enter the choice:4
Subtraction is:
0 0
0 0
**********MENU***************
0. Exit
1. Accept Matrix
2. Display Matrix
3. Sum of Matrix
4. Subtraction of matrix
5. Multiplication of Matrix
6. Transpose of Matrix
*****************************
enter the choice:5
Multiplication is:
7 10
15 22
**********MENU***************
0. Exit
1. Accept Matrix
2. Display Matrix
3. Sum of Matrix
4. Subtraction of matrix
5. Multiplication of Matrix
6. Transpose of Matrix
*****************************
enter the choice:6

Transpose of First Matrix
1 3
2 4

Transpose of Second Matrix
1 3
2 4
**********MENU***************
0. Exit
1. Accept Matrix
2. Display Matrix
3. Sum of Matrix
4. Subtraction of matrix
5. Multiplication of Matrix
6. Transpose of Matrix
*****************************
enter the choice:0
"""