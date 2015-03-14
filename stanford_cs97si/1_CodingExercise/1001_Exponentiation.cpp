#include <iostream>
#include <string>
#include <stdio.h>
#include <cmath>
#include <iomanip>
#include <vector>
#include <assert.h> 
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;

VI sum_vi(vector<int> a, vector<int> b, int* dot_position) {
	VI res;
	int carry = 0;
	int part_sum_res = 0;
	int full_digit_sum = 0;
	int i = 0;
	int j = 0;
	//cout << "asize" << a.size();
	for (; i < a.size() && j < b.size(); i++, j++) {

		full_digit_sum = (b[j] + a[i] + carry);
		//cout << "full" << full_digit_sum;
		part_sum_res = full_digit_sum % 10;
		carry = full_digit_sum - part_sum_res;
		//cout << "part push" << part_sum_res; 
		res.push_back(part_sum_res);
	}

	if (i != a.size()) {
		for (; i < a.size(); i++) {
			res.push_back(a[i]);
		}

	}

	if (j != b.size()) {
		for (; j < b.size(); j++) {
			res.push_back(b[j]);
		}

	}
	//find the dot

	return res;
	//add the dot somewhere, its int array no dot.. :(
}

string calculate_power_string(vector<int> a, vector<int> b) {
	VVI res;
	int t = 0;
	int carry = 0;
	std::vector<int>::iterator it;
	int full_mult_res = 0;
	int part_mult_res = 0;
	for (int j = b.size() - 1; j >= 0; j--) {
		for (int i = a.size() - 1; i >= 0; i--) {

			it = res[t].end();
			full_mult_res = b[j] * a[i] + carry;
			if (i != 0)
				part_mult_res = full_mult_res % 10;
			else
				part_mult_res = full_mult_res;
			carry = full_mult_res - part_mult_res;
			res[t].insert(it, part_mult_res);

		}
	}
	return "";
}

vector<int> num_to_vector(string str_a, int* dot_position) {
	vector<int> res;
	int dot_pos;
	for (int i = 0; i < str_a.length(); i++) {
		if (isdigit(str_a[i]))
			res.push_back(str_a[i] - '0');
		else
			*dot_position = i;
	}
	return res;
}

void test() {

	vector<int> a;
	vector<int> b;
	vector<int> c;
	int pos = 0;
	VI res;

	a.push_back(1);
	a.push_back(2);
	b.push_back(1);
	b.push_back(2);
	c.push_back(2);
	c.push_back(4);
	res = sum_vi(a, b, &pos);
	assert(sum_vi(a, b, &pos) == c);
	a.clear();
	b.clear();
	c.clear();

	a.push_back(1);
	;
	b.push_back(1);
	b.push_back(2);
	c.push_back(2);
	c.push_back(2);
	res = sum_vi(a, b, &pos);
	assert(sum_vi(a, b,&pos) == c);
	a.clear();
	b.clear();
	c.clear();

	a.push_back(1);
	a.push_back(2);
	b.push_back(1);
	c.push_back(2);
	c.push_back(2);
	res = sum_vi(a, b, &pos);
	assert(sum_vi(a, b, &pos) == c);
	a.clear();
	b.clear();
	c.clear();
//	for (int i = 0; i < res.size(); i++) {
//		cout << "res" << res[i] << " ";
//	}
	c.push_back(1);
	c.push_back(0); 
	vector<int> w = num_to_vector(to_string(10), &pos);
	for (int i = 0; i < w.size(); i++) {
		cout << w[i];
	}
	assert(w == c);

	c.clear();
	c.push_back(1);
	c.push_back(0);
	c.push_back(3);
	w = num_to_vector(to_string(10.3), &pos);
	for (int i = 0; i < w.size(); i++) {
		cout << "resu" << w[i] << endl;
	}
	//assert(w == c);
	assert(pos == 2);

	
	
	
}

int main() {
	test();

	//assert (sum_vi({1,2,3}, {1,2,3}, nullptr) == ({1,2,3}));	
	//vector<char> w = int_to_string_vector(10);

//for (int i = 0; i < w.size(); i++) {
//	cout << w[i];
//}
//	int n = 0;
//	double r = 0;
//
//    std::vector<double> res;
//    std::vector<double> r;
//	
//	while(cin>>r>>n)
//	{
//		res = int_to_string_vector(1);
//		res = int_to_string_vector(r);
//		int t = 1;
//		while(t <= n){
//			res = calculate_power_string(std::to_string(r),res);
//			t+=1;
//		}
//	}
	return 0;
}



