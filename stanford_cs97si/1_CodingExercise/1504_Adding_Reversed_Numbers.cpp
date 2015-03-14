#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int reverse_num(int num) {
	int reversed = 0;
	while (num) {
		reversed = reversed * 10 + num % 10;
		num = num / 10;
	}
	return reversed;
}
int main() {
	int t = 0;
	cin >> t;
	int a, b;
	int i = 0;
	while (t--) {
		cin >> a >> b;
		i += 1;
		cout << reverse_num(reverse_num(a) + reverse_num(b)) << endl;
	}
	return 0;
}
