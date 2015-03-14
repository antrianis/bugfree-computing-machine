#include <iostream>
#include <string>
#include <stdio.h>
#include <cmath>
using namespace std;

void get_slice(int current_middle, int dim, int max_gas, int slice_no) {
	cout << "slice #" << slice_no << ":" << endl;
	for (int i = 0; i < dim; ++i) {
		for (int j = 0; j < dim; ++j) {
			int distance = std::abs(j - dim / 2) + abs(i - dim / 2);
			if (distance <= (max_gas - current_middle))
				cout << abs(distance + current_middle);
			else
				cout << ".";
		}
		cout << endl;
	}
}

int main() {
	int t = 0;
	int n = 0;
	int slice = 0;
	int k = 0;
	cin >> t;

	while (k < t) {
		cin >> n;
		int dim = n * 2 + 1;
		cout << "Scenario #" << k + 1 << ":" << endl;
		slice = 0;
		for (int i = n; i >= 0; --i) {
			++slice;
			get_slice(i, dim, n, slice);
		}
		for (int i = 1; i <= n; i++) {
			++slice;
			get_slice(i, dim, n, slice);
		}
		++k;
		if (!(k == t))
			cout << endl;
	}

	return 0;
}

