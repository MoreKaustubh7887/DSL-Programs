"""
Write a python program to store marks scored in subject Fundamental of
Data Structure by N students in the class. Write functions to compute following:
a)	The average score of class 
b)	Highest score and lowest score of class 
c)	Count of students who were absent for the test
d)	Display mark with highest frequency
"""

A= []
main=1
while main:
	print("************MENU****************")
	print("0. Exit")
	print("1. Accept Mark")
	print("2. Display Mark")
	print("3. Average Mark")
	print("4. Highest and Lowest Mark")
	print("5. Absent Student")
	print("6. Highest Frequency")
	print("********************************")
	ch=int(input("Enter the Choice:"))
	
	if ch==1:
		n = int(input("Enter the Number of Student :"))
		for i in range (n):
			while True:
				x = input("Enter the Marks %d:"%(i+1))
				if (x=="AB"):
					x = -1
					break
				x = int(x)
				if ( x >=0 and x <= 50 ):
					break
				else :
					print("Enter the Valid Marks")
			A.append(x)
		print("Marks Accepted & Stored Successfully");

	elif ch==2:
		print("\nMarks of Students:")
		for i in range(len(A)):
			if (A[i] == -1):
				print("Student %d : AB"%(i+1))
			else:
				print("Student %d : %d"%(i+1,A[i]))
		
	elif ch==3:
		Sum = 0
		for i in range (len(A)):
			if (A[i] != -1):
				Sum = Sum + A[i]
		avg = Sum / len(A)
		print("Average Mark of Student is :",avg)
		
		
	elif ch==4:
		Max= -1
		Min= 31
		for i in range (1,len(A)):
			if (Max < A[i]):
				Max = A[i]
			if (A[i] < Min and A[i] != -1):
				Min = A[i]
		print("Highest Mark Score of Class is:",Max)
		print("Lowest Mark Score of Class is:",Min)

		
	elif ch==5:
		count = 0
		for i in range (len(A)):
			if (A[i]== -1):
				count += 1
		print("Absent Student is ",count)
	
	elif ch==6:
		freq = 0
		for i in range (len(A)):
			count = 0
			if (A[i] != -1):
				for j in range (len(A)):
					if(A[i] == A[j]):
						count += 1
			if(freq < count):
				marks = A[i]
				freq = count
		print("\nMarks %d have Highest Frequency %d"%(marks,freq))
		
	elif ch == 0:
		main=0
		
	else:
		print("Enter the Valid Choice")

"""
OUTPUT:
************MENU****************
0. Exit
1. Accept Mark
2. Display Mark
3. Average Mark
4. Highest and Lowest Mark
5. Absent Student
6. Highest Frequency
********************************
Enter the Choice:1
Enter the Number of Student :10
Enter the Marks 1:45
Enter the Marks 2:33
Enter the Marks 3:26
Enter the Marks 4:46
Enter the Marks 5:47
Enter the Marks 6:AB
Enter the Marks 7:AB
Enter the Marks 8:50
Enter the Marks 9:12
Enter the Marks 10:11
Marks Accepted & Stored Successfully
************MENU****************
0. Exit
1. Accept Mark
2. Display Mark
3. Average Mark
4. Highest and Lowest Mark
5. Absent Student
6. Highest Frequency
********************************
Enter the Choice:2

Marks of Students:
Student 1 : 45
Student 2 : 33
Student 3 : 26
Student 4 : 46
Student 5 : 47
Student 6 : AB
Student 7 : AB
Student 8 : 50
Student 9 : 12
Student 10 : 11
************MENU****************
0. Exit
1. Accept Mark
2. Display Mark
3. Average Mark
4. Highest and Lowest Mark
5. Absent Student
6. Highest Frequency
********************************
Enter the Choice:3
Average Mark of Student is : 27.0
************MENU****************
0. Exit
1. Accept Mark
2. Display Mark
3. Average Mark
4. Highest and Lowest Mark
5. Absent Student
6. Highest Frequency
********************************
Enter the Choice:4
Highest Mark Score of Class is: 50
Lowest Mark Score of Class is: 11
************MENU****************
0. Exit
1. Accept Mark
2. Display Mark
3. Average Mark
4. Highest and Lowest Mark
5. Absent Student
6. Highest Frequency
********************************
Enter the Choice:5
Absent Student is  2
************MENU****************
0. Exit
1. Accept Mark
2. Display Mark
3. Average Mark
4. Highest and Lowest Mark
5. Absent Student
6. Highest Frequency
********************************
Enter the Choice:6

Marks 45 have Highest Frequency 1
************MENU****************
0. Exit
1. Accept Mark
2. Display Mark
3. Average Mark
4. Highest and Lowest Mark
5. Absent Student
6. Highest Frequency
********************************
Enter the Choice:0
"""