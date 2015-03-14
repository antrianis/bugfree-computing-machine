#include <iostream>
#include <iostream>
#include <string>
#include <stdio.h>
#include <cmath>
#include <iomanip>
#include <vector>
#include <assert.h> 
using namespace std;

typedef vector<int> VI;
typedef vector<double> VF;
typedef vector<VI> VVI;


int main() {
    int n,r;
    double v;
    int t;

    while (cin >> n && n > 0) {
        r = 0;
        double current_fastest = 0;
        double arrival_time = 0;
        while (r < n) {
            cin >> v;
            cin >> t;    
            if (t >= 0){
                arrival_time = 4.5 * 60 * 60 / v + t;
                if (arrival_time < current_fastest || current_fastest == 0)
                	current_fastest = arrival_time;
            }
            ++r;
        }
        cout << ceil(current_fastest) << endl;
    }
    return 0;
}


