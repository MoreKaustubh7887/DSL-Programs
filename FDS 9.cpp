/*
A palindrome is a string of character that‘s the same forward and backward. Typically, punctuation, capitalization, and spaces are ignored. For example, “Poor Dan is in a
droop” is a palindrome, as can be seen by examining the characters “poor danisina droop” and observing that they are the same forward and backward. One way to check
for a palindrome is to reverse the characters in the string and then compare with them the original-in a palindrome, the sequence will be identical. Write C++ program with functions
a) To print original string followed by reversed string using stack 
b) To check whether given string is palindrome or not
*/


#include<iostream>
#include<ctype.h>
#include<string.h>
using namespace std;
# define MAX 50


class Stack
{
	public:
		char str[MAX],temp[MAX],data[MAX];
		int top= -1,count=0,length=0;
		
		void getString();
		void extractString();
		void Displayreverse();
		void Display();
		void palimdrome();
		void pushdata(char);
		char popdata();
};

void Stack::getString()
{
	cout<<"Enter the string:";
	cin.getline(str,MAX);
	
	length=strlen(str);
}

void Stack::extractString()
{
	int j=0;
	for (int i=0;i<length;i++)
	{
		if(isalpha(str[i]))
		{
			str[j]=tolower(str[i]);
			j++;
		}
	}
	length=j;
	
	for(int i=0;i<length;i++)
	{
		cout<<str[i];
	}
}

void Stack::Displayreverse()
{
	for(int i=length-1;i>=0; i--)
	{
		cout<<str[i];
	}
}

void Stack::palimdrome()
{
	for(int i=0;i<length;i++)
		pushdata(str[i]);
	
	for(int i=0;i<length;i++)
	{
		if(str[i]==popdata())
			count++;
	}
	
	if(count==length)
	{
		for(char i=0;i<length;i++)
		{
			if(str[i]==temp[i]);
		}
		cout<<"\n String is Palimdrome";
	}
	else
		cout<<"\n String is Not Palimdrome";
}

void Stack::pushdata(char temp)
{
	if(top==MAX-1)
	{
		cout<<"\n Stack Overflow";
		return;
	}
	top++;
	data[top]=temp;
	
}

char Stack::popdata()
{
	if(top== -1)
	{
		cout<<"\n Stack Underflow";
		return 0;
	}
	char temp=data[top];
	top--;
	return temp;
}

void Stack::Display()
{
	cout<<"Original String:"<<str;
}

int main()
{
	Stack s;
	s.getString();
	s.Display();
	cout<<"\n Extracted String:";
	s.extractString();
	cout<<"\n Reverse String:";
	s.Displayreverse();
	s.palimdrome();
	
	return 0;
}

/*
Output
Enter the string:Poor Dan is in a droop
Original String:Poor Dan is in a droop
 Extracted String:poordanisinadroop
 Reverse String:poordanisinadroop
 String is Palimdrome
--------------------------------
*/
