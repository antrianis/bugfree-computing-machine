#include <iostream>

using namespace std;

int count_ways(int cows) {
	int ways = 0;
	int sum = 0;
	int j = 0;
	for (int i = 1; i <= cows; i++) {
		j = i;
		do {
			sum += j;
			j += 1;
		} while (sum < cows);
		if (sum == cows) {
			ways += 1;
		}
		sum = 0;
	}
	return ways;
}

int main() {
	int cows = 0;
	cin >> cows;
	cout << count_ways(cows);
	return 0;
}
