#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	int n;
	string str;
	vector<int> stack;

	cin >> n;
	cin.ignore();
	for (int i = 0; i < n; i++) {
		getline(cin, str);

		if (str.compare("top") == 0) {
			if (stack.empty() == true)
				cout << "-1" << endl;
			else
				cout << stack.back() << endl;
		}
		else if (str.compare("size") == 0)
			cout << stack.size() << endl;
		else if (str.compare("empty") == 0) {
			if (stack.empty() == true)
				cout << "1" << endl;
			else
				cout << "0" << endl;
		}
		else if (str.compare("pop") == 0) {
			if (stack.empty() == true)
				cout << "-1" << endl;
			else {
				cout << stack.back() << endl;
				stack.pop_back();
			}
		}
		else {
			stack.push_back(stoi(str.substr(5)));
		}
	}
	

	return 0;
}