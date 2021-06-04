#include <iostream>
#define ll long long
using namespace std;

bool Panoramixs_Prediction()
{   int prime_numbers[] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47};
    ll prime,next_prime;
    cin>>prime>>next_prime;
    for(int i = 0; i < 15;i++)
    {
        if(prime_numbers[i] > prime )
        {
            if(prime_numbers[i] == next_prime)
               return true;
            else
               return false;
        }
    }
    return false;
    
    

}
int main() {
	int remained_test_cases = 1 ;
// 	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   if(Panoramixs_Prediction())
	    cout<<"YES";
	    else
	    cout<<"NO";
	    
	    remained_test_cases--;
	}
	return 0;
}
