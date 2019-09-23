#include<iostream>
using namespace std;
class Test{

	int on,off;
	public:
	Test()
	{
		on  = 1;
		off = 0;
	}
	Test(const Test &t)
	{
		on = t.on;
		off = t.off;
	}
	void show(int on,int off){
		this->on = on;
		this->off = off;
	}
	void glow(){
		cout<<"Glow"<<on<<"\t"<<off<<endl;
	}
	~Test()
	{
		cout<<"Destructor Invoked\n\n";
	}
};



int main()
{
	Test t; //Object Creation
	
	t.show(2,3);
	t.glow();
	cout<<"Size of Object is: "<<sizeof(t)<<endl;
	
	Test t1 (t);
	t1.glow();
	
	return 0;
}
