#include <bits/stdc++.h>
#define ll long long
using namespace std;

ll Creating_the_Contest()
{  ll total_problems;
   cin>>total_problems;
   vector<ll> diff_of_prob;
   
   for(int i = 0;i<total_problems;i++)
   {   ll A;
       cin>>A;
       diff_of_prob.push_back(A);
   }
   
   ll max_length = 1;
   ll count = 0;
   for(int i = 0; i < total_problems-1;i++)
   {
       if(diff_of_prob[i+1] <= diff_of_prob[i]*2)
           count += 1;
       else
       {
           max_length = max(max_length,count+1);
           count = 0;
       }
   }
   max_length = max(max_length,count+1);
   return (max_length);
   
}


int main() {
	int remained_test_cases = 1 ;
// 	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   cout<<Creating_the_Contest()<<"\n";
	    remained_test_cases--;
	}
	return 0;
}
