#include <bits/stdc++.h>
#define ll long long
using namespace std;

ll Number_of_pairs()
{ ll N,L,R;
  cin>>N>>L>>R;
  vector<ll> array;
  
  for(ll i = 0;i<N;i++)
    {  ll a;
        cin>>a;
        array.push_back(a);
    }
  sort(array.begin(), array.end());
  ll pairs_possible = 0;
  for(ll i = 0;i < N;i++)
  {
      if(array[i] >=R)
      continue;
      ll lower = lower_bound(array.begin() + i + 1, array.end(), max(0ll,L - array[i])) - array.begin();
      ll upper = upper_bound(array.begin()+ i + 1, array.end(),R - array[i]) - array.begin();
      pairs_possible += max(0ll,upper - lower);
      
      
  }
  return pairs_possible;
  
}


int main() {
	int remained_test_cases = 1 ;
	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   cout<<Number_of_pairs()<<"\n";
	    remained_test_cases--;
	}
	return 0;
}