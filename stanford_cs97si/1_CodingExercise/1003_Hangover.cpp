#include <iostream>

using namespace std;

int main() {
    double c, s;
    int i;
    while(cin>>c&&c>0.0) {
        s = 0.0;
        i = 1;
        while(s < c) {
            s+=1.0/++i;
        }
        cout<<i-1<< " card(s)"<<endl;
    }

    return 0;
}


