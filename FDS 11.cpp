/*
Queues are frequently used in computer programming, and a typical example is the creation of a job queue by an operating system. If the operating system does not use
priorities, then the jobs are processed in the order they enter the system. Write C++ program for simulating job queue. Write functions to add job and delete job from queue.
*/


#include<iostream>
#define MAX 10
using namespace std;

class Queue
{
	int front,rear;
	int job[MAX];
	
	public:
		Queue()
		{
			front=rear=-1;
		}
		int isfull();
		int isempty();
		void enqueue(int);
		int Delqueue();
		void display(); 
};

int Queue::isfull()
{
	if(rear==MAX-1)
		return(1);
	else
		return(0);
}

int Queue::isempty()
{
	if(front==rear==-1)
		return(1);
	else
		return(0);
}

void Queue::enqueue(int x)
{
	job[++rear]=x;
}

int Queue::Delqueue()
{
	return job[++front];
}

void Queue::display()
{
	for(int i=front+1;i<=rear;i++)
		cout<<job[i]<<" ";
	
}

int main ()
{
	Queue obj;
	char ch;
	int choice,x;
	
	do 
	{
		cout<<"\n**********MENU***************\n1. insert job \n2. Delete job \n3. Display \n4. Exit \n****************************\n";
		cout<<"enter the choice:";
		cin>>choice;
		
		switch(choice)
		{
			case 1:
				if(obj.isfull()==0)
				{
					cout<<"enter the job:";
					cin>>x;
					obj.enqueue(x);
				}
				else
				{
					cout<<"\nQueue Overflow";
				}
				break;
			
			case 2:
				if(obj.isempty()==0)
				{
					obj.Delqueue();
				}
				else
				{
					cout<<"\nQueue underflow ";
				}
				cout<<"\nRemaining Jobs:";
				obj.display();
				break;
			
			case 3:
				if(obj.isempty()==0)
				{
					cout<<"\nQueue Containing:\n";
					obj.display();
				}
				else
				{
					cout<<"\nQueue underflow ";
				}
				break;
			
			case 4:
				exit(0);
				
			default:
				cout<<"Wrong Choice";
		}
		cout<<"\n\ndo you want to continue:";
		cin>>ch;
		
	}while(ch=='y'||ch=='Y');
	
	
	return 0;
}

/*
OUTPUT

**********MENU***************
1. insert job
2. Delete job
3. Display
4. Exit
****************************
enter the choice:1
enter the job:43


do you want to continue:y

**********MENU***************
1. insert job
2. Delete job
3. Display
4. Exit
****************************
enter the choice:3

Queue Containing:
43

do you want to continue:y

**********MENU***************
1. insert job
2. Delete job
3. Display
4. Exit
****************************
enter the choice:1
enter the job:22


do you want to continue:y

**********MENU***************
1. insert job
2. Delete job
3. Display
4. Exit
****************************
enter the choice:1
enter the job:34


do you want to continue:y

**********MENU***************
1. insert job
2. Delete job
3. Display
4. Exit
****************************
enter the choice:1
enter the job:23


do you want to continue:y

**********MENU***************
1. insert job
2. Delete job
3. Display
4. Exit
****************************
enter the choice:1
enter the job:23


do you want to continue:y

**********MENU***************
1. insert job
2. Delete job
3. Display
4. Exit
****************************
enter the choice:3

Queue Containing:
43 22 34 23 23

do you want to continue:y

**********MENU***************
1. insert job
2. Delete job
3. Display
4. Exit
****************************
enter the choice:3

Queue Containing:
43 22 34 23 23

do you want to continue:y

**********MENU***************
1. insert job
2. Delete job
3. Display
4. Exit
****************************
enter the choice:2

Remaining Jobs:22 34 23 23

do you want to continue:y

**********MENU***************
1. insert job
2. Delete job
3. Display
4. Exit
****************************
enter the choice:2

Remaining Jobs:34 23 23

do you want to continue:y

**********MENU***************
1. insert job
2. Delete job
3. Display
4. Exit
****************************
enter the choice:2

Remaining Jobs:23 23

do you want to continue:y

**********MENU***************
1. insert job
2. Delete job
3. Display
4. Exit
****************************
enter the choice:2

Remaining Jobs:23

do you want to continue:n

*/
