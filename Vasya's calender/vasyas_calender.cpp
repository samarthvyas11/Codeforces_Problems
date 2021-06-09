#include <bits/stdc++.h>
#define ll long long
using namespace std;

int Vasyas_Calendar()
{ ll day_limit ;
  cin>>day_limit;
  ll months;
  cin>>months;
  ll days_in_months[months];
  
  for(ll i = 0;i<months;i++)
    cin>>days_in_months[i];
  
  ll ongoing_day = days_in_months[0] + 1 ;
  if(days_in_months[0] == day_limit)
      ongoing_day = 1 ;
  ll increase = 0;
  
  
  for(ll m = 1;m < months;m++)
  {
      if(ongoing_day != 1)
      { increase += day_limit - ongoing_day + 1 ;
        ongoing_day = 1 ;
      }
      ongoing_day += days_in_months[m];
  }
  
  return (increase);
}


int main() {
	int remained_test_cases = 1 ;
// 	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   cout<<Vasyas_Calendar();
	    remained_test_cases--;
	}
	return 0;
}
