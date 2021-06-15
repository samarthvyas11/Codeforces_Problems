#include <bits/stdc++.h>
#define ll long long
using namespace std;


ll Histogram_Ugliness()
{ ll total_bars;
  cin>>total_bars;
  vector<ll> bars;
  
  
  
  for(ll i = 0;i < total_bars;i++)
  {   ll height;
      cin>>height;
      bars.push_back(height);
  }
  if (total_bars == 1)
  return(bars[0]);
  
  ll ugliness = 0;
  ll last = 0;     //previous height
  for(ll i = 0;i < total_bars;i++)
  {
      if(bars[i] > last)
      {  ugliness += bars[i] - last;
         
      }
      
      if (i == total_bars - 1)
      {ugliness += bars[i];
      break;}
      
      if (bars[i+1] < bars[i])
       ugliness += bars[i] - bars[i+1];
       
       last = bars[i];
       
  }
  
  for(ll  i = 0;i< total_bars;i++)
  {  if(i == 0)
     {
         if(bars[i+1] < bars[i])
         {
             ugliness -= bars[i] - bars[i+1];
             bars[i] = bars[i+1];
         }
     }
     else if(i == total_bars - 1 )
     {
         if(bars[i] > bars[i-1])
         {
             ugliness -= bars[i] - bars[i-1];
             bars[i] = bars[i-1];
         }
     }
     else
     {
         if(bars[i] > bars[i-1] && bars[i] > bars[i+1])
         {
             ugliness -= bars[i] - max(bars[i+1],bars[i-1]);
             bars[i] = max(bars[i-1],bars[i+1]);
         }
     }
      
  }
  return (ugliness);
  

}


int main() {
	int remained_test_cases = 1 ;
	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   cout<<Histogram_Ugliness()<<"\n";
	    remained_test_cases--;
	}
	return 0;
}
