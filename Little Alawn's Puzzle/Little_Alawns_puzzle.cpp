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

ll Little_Alawns_Puzzle()
{ 
  ll len_array;
  cin>>len_array;
  vector<ll> array1;
  vector<ll> array2;
  vector<bool> done;
  ll index1[len_array];
  ll index2[len_array];
  
  for(ll i = 0 ;i < len_array;i++)
  {index2[i] = -1;
    index1[i] = -1;}
  
  for(ll i = 0;i< len_array;i++)
  {   ll a1;
      cin>>a1;
      index1[a1-1] = i;
      done.push_back(false);
      array1.push_back(a1);
  }
 
  for(ll i = 0;i < len_array;i++)
  {  ll a2;
     cin>>a2;
     index2[a2-1] = i;
     array2.push_back(a2);
  }
 
 
  ll pairs = 0;
  for(ll i = 0;i < len_array;i++)
  { if(!done[i])
    { ll start = array2[i];
      ll at_index = i;
      while (array1[at_index] != start)
      {
          done[at_index] = true;
          at_index = index2[array1[at_index]-1];
      }
      done[at_index] = true;
      pairs++;
    }
  }
  
  return (power(2,pairs)%1000000007);

}


int main() {
	int remained_test_cases = 1 ;
	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   cout<<Little_Alawns_Puzzle()<<"\n";
	    remained_test_cases--;
	}
	return 0;
}
