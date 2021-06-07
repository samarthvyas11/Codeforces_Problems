#include <bits/stdc++.h>
#define ll long long
using namespace std;

int Petr_and_Book()
{ ll pages_to_read;
  cin>>pages_to_read;
  ll page_on_day[7];

  for(int day = 0;day < 7;day++)
     cin>>page_on_day[day];
  ll day = 0;     

  while(pages_to_read > 0)
  {   
      pages_to_read -= page_on_day[day];
      if (pages_to_read <= 0)
       return (day+1);
      day += 1;
      if (day >= 7)
      day = 0;
      
      
  }
}


int main() {
	int remained_test_cases = 1 ;
// 	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   cout<<Petr_and_Book();
	    remained_test_cases--;
	}
	return 0;
}
