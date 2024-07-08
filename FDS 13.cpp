/*
A double-ended queue (deque) is a linear list in which additions and deletions may be made at either end. Obtain a data
representation mapping a deque into a one-dimensional array. Write C++ program to simulate deque with functions to add 
and delete elements from either end of the deque. 
*/

#include <iostream>
using namespace std;

const int Max = 10;
int deque[Max];
 
int front = -1;
int rear = -1;
 
bool isEmpty() 
{
    if (front == -1) 
	{
        return true;
    }
    return false;
}
 
bool isFull() 
{
    if ((rear + 1) % Max == front) 
	{
        return true;
    }
    return false;
}

void insertFront(int x) 
{
    if (!isFull()) 
	{
        if (front == -1) 
		{
            front = rear = 0;
            deque[front] = x;
        } 
        else 
		{
            if (front == 0) 
			{
                front = Max - 1;
            } 
			else 
			{
                front--;
            }  
            deque[front] = x;
        }
    }
}
void insertRear(int x) 
{
    if (!isFull()) 
	{
        if (rear == -1) 
		{
            front = rear = 0;
            deque[rear] = x;
        } 
        else 
		{
            if (rear == Max - 1) 
			{
                rear = 0;
            } 
			else 
			{
                rear++;
            }
            deque[rear] = x;
        }
    }
}
void deleteFront() 
{
    if (!isEmpty()) 
	{
        if (front == rear) 
		{
            front = rear = -1;
        } 
        else 
		{
            if (front == Max - 1) 
			{
                front = 0;
            } 
			else 
			{
                front++;
            }
        }
    }
}
void deleteRear() 
{
    if (!isEmpty()) 
	{
        if (front == rear) 
		{
            front = rear = -1;
        } 
        else 
		{
            if (rear == 0) 
			{
                rear = Max - 1;
            } 
			else 
			{
                rear--;
            }
        }
    }
}
int getFront() 
{
    if (!isEmpty()) 
	{
        return deque[front];
    }
    return -1;
}

int getRear() 
{
    if (!isEmpty()) 
	{
        return deque[rear];
    }
    return -1;
}
int main() 
{
    insertFront(5);
    insertRear(10);
    insertRear(11);
    insertFront(19);
    cout<<getFront()<<endl;
    cout<<getRear()<<endl;
	if (isEmpty()) 
	{
        cout<<"true"<<endl;
    } 
	else 
	{
        cout<<"false"<<endl;
    }
    deleteRear();
    cout<<getRear()<<endl;
    deleteFront();
    cout<<getFront()<<endl;
    if (isEmpty()) 
	{
        cout<<"true"<<endl;
    } 
	else 
	{
        cout<<"false"<<endl;
    }
    deleteRear();
    cout<<getRear()<<endl;
    deleteFront();
    cout<<getFront()<<endl;
    if (isEmpty()) 
	{
        cout<<"true"<<endl;
    } 
	else 
	{
        cout<<"false"<<endl;
    }
    return 0;
}


/*OUTPUT:
19
11
false
10
5
false
5
-1
true
*/
