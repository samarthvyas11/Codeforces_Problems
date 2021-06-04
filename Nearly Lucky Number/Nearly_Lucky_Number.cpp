#include <iostream>
#define ll long long
using namespace std;

bool Nearly_Lucky_Number()
{
    ll number;
    cin>>number;
    int count_luck_numbers = 0;
    while(number > 0)
    { int digit = number % 10;
      if(digit == 4 || digit == 7)   //4 and 7 are lucky numbers
      count_luck_numbers++;
      number = number / 10;    
    }
    if(count_luck_numbers == 4 || count_luck_numbers == 7)
    return true;
    
    return false;

}
int main() {
	int remained_test_cases = 1 ;
// 	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   if (Nearly_Lucky_Number())
	    cout<<"YES";
	    else
	    cout<<"NO";
	    remained_test_cases--;
	}
	return 0;
}
