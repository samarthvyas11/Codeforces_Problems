#include <bits/stdc++.h>
#define ll long long
using namespace std;

long long power(long long x, long long y) { 
    long long res = 1;
    ll MOD= 1000000007;
    x = x % MOD;
    while (y > 0) { 
        if (y & 1) 
            res = (res*x) % MOD; 
        y = y>>1;
        x = (x*x) % MOD; 
    } 
    return res; 
}

ll Plant()
{ ll years;
cin>>years;

if (years == 0)
return (1);

return ((power(2,years-1) + power(2,2*years - 1))% 1000000007);
  
}


int main() {
	int remained_test_cases = 1 ;
// 	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   cout<<Plant();
	    remained_test_cases--;
	}
	return 0;
}
