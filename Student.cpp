//Getter and Setter in CPP
#include<iostream>
using namespace std;

class Student
{
	int roll;
	string name;
	
	public:
	void setRoll(int roll)
	{
		this->roll = roll;
	}
	int getRoll()
	{
		return roll;
	}
	void setName(string name)
	{
		this->name = name;
	}
	string getName()
	{
		return name;
	}
};

int main()
{
	Student s;
	s.setRoll(101);
	cout<<s.getRoll()<<endl;
}
