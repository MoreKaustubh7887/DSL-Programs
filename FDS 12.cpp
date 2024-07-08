/*
Pizza parlor accepting maximum M orders. Orders are served in first come first served basis. Order once placed can not be cancelled. 
Write C++ program to simulate the system using circular queue using array.
*/

#include<iostream>
#include<cstdlib>
using namespace std;

class pizza
{
	public:
		int front,rear;
		int order[5];
		
		pizza()
		{
			front=-1;
			rear=-1;
		}
		
		int isfull()
		{
			if(front==0&&rear==4||front==rear+1)
				return (1);
			else 
				return(0);
		}
		
		
		int isempty()
		{
			if(front==rear==-1)
				return(1);
			else
				return(0);
		}
		
		
		void add()
		{
			if(isfull()==0)
			{
				char c;
				do
				{
					cout<<"\n enter the ID:";
				
					if(front==-1&&rear==-1)
					{
						
						front=0;
						rear=0;
						cin>>order[rear];
					}
					else
					{
						rear=(rear+1)%5;
						cin>>order[rear];
						
					}
					cout<<"\n Do you want to add :";
					cin>>c;
				}while(c=='y'||c=='Y');
			}
			else
				cout<<"\n Order are full";
		}
		
		
		int serve()
		{
			if(isempty()==0)
			{
				if(front==rear)
				{
					cout<<"\n order are served:"<<order[front];
					front=-1;
					rear=-1;
				}
				else
				{
					cout<<"\n order are served:"<<order[front];
					front=(front+1)%5;
				}
			}
			else
			{
				cout<<"\n order are empty";
			}
		}
		
		
		void display()
		{
			if(isempty()==0)
			{
				for(int i=front;i!=rear;i=(i+1)%5)
					cout<<order[i]<<" <- ";
				cout<<order[rear];	
			}
			else
			{
				cout<<"\n order are empty";
			}
		}
};

int main()
{
	pizza p;
	int choice;
	char ch;
	do
	{
		cout<<"\n*********MENU*********";
		cout<<"\n1. Get Order";
		cout<<"\n2. Display Orders";
		cout<<"\n3. Serve Order";
		cout<<"\n4. Exit";
		cout<<"\n**********************";
		cout<<"\n enter the choice:";
		cin>>choice;
		
		switch(choice)
		{
			case 1:
				p.add();
				break;
			case 2:
				p.display();
				break;
			case 3:
				p.serve();
				break;
			case 4:
				exit(0);
			default:
				cout<<"\nwrong choice";
		}
		cout<<"\n do you want to continue:";
		cin>>ch;
	}while(ch=='y'||ch=='Y');
	
	return 0;
}

/*
Output

*********MENU*********
1. Get Order
2. Display Orders
3. Serve Order
4. Exit
**********************
 enter the choice:1

 enter the ID:546457

 Do you want to add :y

 enter the ID:234325

 Do you want to add :n

 do you want to continue:y

*********MENU*********
1. Get Order
2. Display Orders
3. Serve Order
4. Exit
**********************
 enter the choice:2
546457 <- 234325
 do you want to continue:y

*********MENU*********
1. Get Order
2. Display Orders
3. Serve Order
4. Exit
**********************
 enter the choice:3

 order are served:546457
 do you want to continue:y

*********MENU*********
1. Get Order
2. Display Orders
3. Serve Order
4. Exit
**********************
 enter the choice:2
234325
 do you want to continue:y

*********MENU*********
1. Get Order
2. Display Orders
3. Serve Order
4. Exit
**********************
 enter the choice:1

 enter the ID:346534

 Do you want to add :y

 enter the ID:463457

 Do you want to add :y

 enter the ID:355532

 Do you want to add :y

 enter the ID:57553

 Do you want to add :n

 do you want to continue:y

*********MENU*********
1. Get Order
2. Display Orders
3. Serve Order
4. Exit
**********************
 enter the choice:2
234325 <- 346534 <- 463457 <- 355532 <- 57553
 do you want to continue:y

*********MENU*********
1. Get Order
2. Display Orders
3. Serve Order
4. Exit
**********************
 enter the choice:1

 Order are full
 do you want to continue:y

*********MENU*********
1. Get Order
2. Display Orders
3. Serve Order
4. Exit
**********************
 enter the choice:4

--------------------------------
*/
