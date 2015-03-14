#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int find_max(int freq[]) {
	int m = 0;
	for (int i = 0; i < 26; i++) {
		if (freq[i] > m) {
			m = freq[i];
		}
	}
	return m;
}
int main() {
	int freq[26] = { };
	string s;
	for (int i = 0; i < 4; ++i) {
		getline(cin, s);
		for (int j = 0; j < int(s.length()); ++j) {
			if (int(s[j]) >= 65 and int(s[j]) <= 91) {
				freq[int(s[j]) - 65] += 1;
			}
		}
	}	
	
	int m = find_max(freq);

	while (m) {
		for (int var = 0; var < 26; ++var) {
			if (freq[var] >= m){
				cout << "* ";
			}
			else
				cout << "  ";
		}
		cout << endl;
		--m;
	}
	for (int var = 0; var < 26; ++var) {
		cout << char(var + 65) << " ";
	}
	return 0;
}

