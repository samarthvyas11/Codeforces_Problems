#include <iostream>
using namespace std;

string Word()
{
    string word;
    cin>>word;
    int first;
    first = word[0];
    if(first >= 97)
    word[0] = char(first-32);
    return word;

}
int main() {
	int remained_test_cases = 1 ;
// 	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   cout<<Word();
	    remained_test_cases--;
	}
	return 0;
}
