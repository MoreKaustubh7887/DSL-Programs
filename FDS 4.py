"""
a)	Write a python program to store names and mobile numbers of your friends
in sorted order on names. Search your friend from list using binary search
(recursive and non-recursive). Insert friend if not present in Phone book

b)	Write a python program to store names and mobile numbers of your friends
in sorted order on names. Search your friend from list using Fibonacci search.
Insert friend if not present in Phone book.
"""

A=[]

def Accept(A):
	n=int(input("Enter the Number of Friend:"))
	print("Input Friends Information in sorted order of Names ")
	for i in range(n):
		print("Enter the %d Friend Name and Number:"%(i+1))
		name=input()
		number=int(input())
		X = [name,number]
		A.append(X)
	print("Data Accepted Successfully")
	return n

def Display(A,n):
	if(n==0):
		print("Phone book is Empty ")
	else:
		print("Friends Information : ")
		for i in range(n):
			print(" Friend %d : %10s %s  "%((i+1),A[i][0],A[i][1]))
		print("\n");

def recursive(A,s,l,X):
	if(s <= l ):
		mid=int((s+l)/2)
		if (A[mid][0] == X):
			return mid
		else :
			if (X < A[mid][0]):
				return recursive(A,s,mid-1,X)
			else:
				return recursive(A,mid +1,l,X)
	return -1

def nonrecursive(A,n,X):
	s=0
	l=n-1
	while(s<=l):
		mid = int ((s + l)/2)
		if (A[mid][0] == X):
			return mid
		else:
			if (X < A[mid][0]):
				l=mid-1
			else :
				s =mid +1
	return -1

def Fibonacci(A,n,X):
	f1=0
	f2=1
	f3=f1+f2
	offset= -1
	while(f3 < n):
		f1=f2
		f2=f3
		f3=f1+f2
	while(f3 > 1):
		i = min(offset+f1,n-1)
		if( A[i][0]==X ):
			return i
		else:
			if( X < A[i][0]):
				f3= f2
				f2= f2-f1
				f1= f3-f2
			else:
				f3=f2
				f2=f1
				f1=f3-f2
				offset = i
	if( f2==1 and (offset+1) < n and A[offset + 1][0]==X):
		return offset+1
	return -1


def insert(A,n,name):
	number= int(input("Enter the Number:"))
	X= [name, number]
	A.append(X)
	j= n-1
	while( j >= 0) :
		if (A[j][0] <= name) :
			break
		else :
			A[j+1] = A[j]
		j = j - 1
	A[j+1] = X
	print("Friend Added")
	Display(A,n+1)


main=1
while main:
	print("************MENU**************")
	print("0. Exit")
	print("1. Accept Phone Book")
	print("2. Recursive Search")
	print("3. Non Recursive Search")
	print("4. Fibonacci Search")
	print("******************************")
	
	ch=int(input("Enter the Choice:"))
	
	if ch==1:
		n=Accept(A)
		Display(A,n)
		
	elif ch==2:
		X= input("Enter the Name :")
		flag = recursive(A,0,n-1,X)
		if (flag == -1):
			print("Friend Not Found")
			insert(A,n,X)
			n=n+1
		else:
			print("Friend Found at Location is %d:"%(flag+1)) 
		
	elif ch==3:
		X= input("Enter the Name :")
		flag = nonrecursive(A,n,X)
		if (flag == -1):
			print("Friend not Found")
			insert(A,n,X)
			n=n+1
		else:
			print("Friend found at location is %d:"%(flag+1))
	
	elif ch==4:
		X= input("Enter the Name :")
		flag = Fibonacci(A,n,X)
		if (flag == -1):
			print("Friend Not Found")
			insert(A,n,X)
			n=n+1
		else:
			print("Friend Found at Location is %d:"%(flag+1))
		
	elif ch==0:
		main=0
	
	else:
		print("Enter Valid Choice")
		
"""
OUTPUT
************MENU**************
0. Exit
1. Accept Phone Book
2. Recursive Search
3. Non Recursive Search
4. Fibonacci Search
******************************
Enter the Choice:1
Enter the Number of Friend:4
Input Friends Information in sorted order of Names
Enter the 1 Friend Name and Number:
aditya
6466877788
Enter the 2 Friend Name and Number:
asim
4557756788
Enter the 3 Friend Name and Number:
atharv
3657688998
Enter the 4 Friend Name and Number:
jatin
8786767676
Data Accepted Successfully
Friends Information :
 Friend 1 :     aditya 6466877788
 Friend 2 :       asim 4557756788
 Friend 3 :     atharv 3657688998
 Friend 4 :      jatin 8786767676


************MENU**************
0. Exit
1. Accept Phone Book
2. Recursive Search
3. Non Recursive Search
4. Fibonacci Search
******************************
Enter the Choice:2
Enter the Name :asim
Friend Found at Location is 2:
************MENU**************
0. Exit
1. Accept Phone Book
2. Recursive Search
3. Non Recursive Search
4. Fibonacci Search
******************************
Enter the Choice:3
Enter the Name :atharv
Friend found at location is 3:
************MENU**************
0. Exit
1. Accept Phone Book
2. Recursive Search
3. Non Recursive Search
4. Fibonacci Search
******************************
Enter the Choice:4
Enter the Name :atharv
Friend found at location is 3:
************MENU**************
0. Exit
1. Accept Phone Book
2. Recursive Search
3. Non Recursive Search
4. Fibonacci Search
******************************
Enter the Choice:4
Enter the Name :sudarshan
Friend Not Found
Enter the Number:4345768878
Friend Added
Friends Information :
 Friend 1 :     aditya 6466877788
 Friend 2 :       asim 4557756788
 Friend 3 :     atharv 3657688998
 Friend 4 :      jatin 8786767676
 Friend 5 :  sudarshan 4345768878
************MENU**************
0. Exit
1. Accept Phone Book
2. Recursive Search
3. Non Recursive Search
4. Fibonacci Search
******************************
Enter the Choice:0
"""