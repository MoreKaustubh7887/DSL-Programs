"""
Write a python program to compute following operations on String:
a)	To display word with the longest length
b)	To determines the frequency of occurrence of particular character in the string
c)	To check whether given string is palindrome or not 
d)	To display index of first appearance of the substring 
e)	To count the occurrences of each word in a given string

"""

main=1
while main:
	print ("  **************************MENU*****************************")
	print ("0 : Exit")
	print ("1 : Display longest Word")
	print ("2 : Frequency of particular character in the string")
	print ("3 : String is palindrome or not ")
	print ("4 : First appearance of the substring")
	print ("5 : Count the occurrences of each word in a given string")
	print ("  ***********************************************************")
	
	ch = int(input("Enter your choice : "))
	
	if (ch == 1) :
		Str = input("Enter the main string : ")
		M_str = ""
		i = 0
		while( i < len(Str)) :
			word = ""
			while(Str[i] != ' ') :
				word += Str[i]
				i = i + 1
				if( i == len(Str)) :
					break
			if(i != len(Str)) :
				while(Str[i] == ' ') :
					i = i + 1
			if(len(M_str) < len(word)) :
				M_str = word
		print("\tWord with longest length is ( %s ) having lenght %d\n\n"%(M_str,len(M_str)))
		
		
	elif (ch == 2) :
		Str = input("Enter the string : ")
		C = input("Enter the character  : ")
		print("\tString : %s"%Str)
		print("\tCharacter : %s"%C)
		count = 0
		for i in range(len(Str)) :
			if(Str[i] == C) :
				count += 1
		print("\tFrequency of occurrence of character(%s) in string(%s) is %d\n\n"%(C,Str,count))
		
		
	elif (ch == 3) :
		Str = input("Enter the string to be checked : ")
		b = 0
		e = len(Str) - 1
		while( b < e) :
			if(Str[b] != Str[e]) :
				break
			b += 1
			e -= 1
		if(b < e) :
			print("\t%s string is not an palindrome string\n\n"%Str)
		else :
			print("\t%s string is an palindrome string\n\n"%Str)
	
	
	elif (ch == 4) :
		M = input("Enter the main string : ")
		S = input("Enter the sub string to check : ")
		print("Main String : %s"%M)
		print("Substring String : %s"%S)
		L1 = len(M)
		L2 = len(S)
		if(L1 >= L2) :
			for i in range((L1 - L2 + 1)) :
				flag = 1
				for j in range(L2):
					if(M[i+j] != S[j]) :
						flag = 0
						break
				if(flag == 1) :
					print("Substring %s found at index %d\n\n"%(S,i))
					break;
			if(flag == 0) :
				print("Substring not found in the main string\n\n")
		else :
			print("Substring is greater than main string\n\n")
	
	
	elif (ch == 5) :
		Str = input("Enter the main string : ") 
		i = 0
		Word_array = []
		Count = []
		while( i < len(Str)) :
			word = ""
			while(Str[i] != ' ') :
				word += Str[i]
				i = i + 1
				if( i == len(Str)) :
					break
			if(i != len(Str)) :
				while(Str[i] == ' ') :
					i = i + 1
			if(len(Word_array) == 0) :
				Word_array.append(word)
				Count.append(1)
			else :
				flag = 1
				for j in range(len(Word_array)) :
					if(Word_array[j] == word) :
						Count[j] += 1
						flag = 0
						break
				if (flag == 1) :
					Word_array.append(word)
					Count.append(1)
		for i in range(len(Word_array)) :
			print("\t%15s : %d "%(Word_array[i],Count[i]))
	
	
	elif (ch == 0):
		print ("End of Program")
		main=0
	
	
	else :
		print ("Enter Valid Choice")

"""
OUTPUT
  **************************MENU*****************************
0 : Exit
1 : Display longest Word
2 : Frequency of particular character in the string
3 : String is palindrome or not
4 : First appearance of the substring
5 : Count the occurrences of each word in a given string
  ***********************************************************
Enter your choice : 1
Enter the main string : Dhoni have Highest fan Following
        Word with longest length is Following having lenght 9


  **************************MENU*****************************
0 : Exit
1 : Display longest Word
2 : Frequency of particular character in the string
3 : String is palindrome or not
4 : First appearance of the substring
5 : Count the occurrences of each word in a given string
  ***********************************************************
Enter your choice : 2
Enter the string : Dhoni have Highest fan Following
Enter the character  : H
        String : Dhoni have Highest fan Following
        Character : H
        Frequency of occurrence of character(H) in string(Dhoni have Highest fan Following) is 1


  **************************MENU*****************************
0 : Exit
1 : Display longest Word
2 : Frequency of particular character in the string
3 : String is palindrome or not
4 : First appearance of the substring
5 : Count the occurrences of each word in a given string
  ***********************************************************
Enter your choice : 3
Enter the string to be checked : madam
        madam string is an palindrome string


  **************************MENU*****************************
0 : Exit
1 : Display longest Word
2 : Frequency of particular character in the string
3 : String is palindrome or not
4 : First appearance of the substring
5 : Count the occurrences of each word in a given string
  ***********************************************************
Enter your choice : 4
Enter the main string : Dhoni have Highest fan Following
Enter the sub string to check : have
Main String : Dhoni have Highest fan Following
Substring String : have
Substring have found at index 6


  **************************MENU*****************************
0 : Exit
1 : Display longest Word
2 : Frequency of particular character in the string
3 : String is palindrome or not
4 : First appearance of the substring
5 : Count the occurrences of each word in a given string
  ***********************************************************
Enter your choice : 5
Enter the main string : Dhoni have Highest fan Following
                  Dhoni : 1
                   have : 1
                Highest : 1
                    fan : 1
              Following : 1
  **************************MENU*****************************
0 : Exit
1 : Display longest Word
2 : Frequency of particular character in the string
3 : String is palindrome or not
4 : First appearance of the substring
5 : Count the occurrences of each word in a given string
  ***********************************************************
Enter your choice : 0
End of Program

"""