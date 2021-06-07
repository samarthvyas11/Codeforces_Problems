#include <bits/stdc++.h>
#define ll long long
using namespace std;

float Drinks()
{ ll total_drinks;
  cin>>total_drinks;
  ll percent_orange_in[total_drinks];
  ll total_volume = 100*total_drinks;
  ll volume_of_orange = 0;
  
  for(int i = 0 ;i < total_drinks;i++ )
  {
      cin>>percent_orange_in[i];
      volume_of_orange += percent_orange_in[i];
  }
  
  float percent_orange = ((float)volume_of_orange/total_volume)*100;
   
   return percent_orange;
  
  
}


int main() {
	int remained_test_cases = 1 ;
// 	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   cout<<Drinks();
	    remained_test_cases--;
	}
	return 0;
}
