#include <iostream>
#include <algorithm>
#include <iterator>
#include <vector>
#include <string>
using namespace std;

int unsortness(string s) {
	int slen = s.length();
	int unsorted = 0;
	int i;
	for (i = 0; i < slen; ++i) {
		char ci = s[i];
		for (int j = i + 1; j < slen; ++j)
			if (ci > s[j])
				unsorted += 1;
	}
	return unsorted;

}

struct compare {
	bool operator()(std::string const& s1, std::string const& s2) {
		int un1 = unsortness(s1);
		int un2 = unsortness(s2);
		if (un1 <= un2)
			return true;
		else
			return false;
	}
};

int main() {
	int t = 0;
	int slen = 0;
	cin >> slen >> t;
	
	string * strings= new string[t];
	for (int i = 0; i < t; ++i) {
		cin >> strings[i];
	}
	
	sort(strings, strings + t, compare());
	for (int i = 0; i < t; ++i) {
		cout << strings[i] << endl;
	}
	delete [] strings;
	return 0;
}
