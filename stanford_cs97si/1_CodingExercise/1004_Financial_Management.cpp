#include <iostream>

using namespace std;

int main()
{
    float f,s;
    f=s=0.0;
    while(cin>>f)
        s+=f;
    cout<<"$"<< s/12.0<<endl;
    return 0;
}
