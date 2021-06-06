#include <bits/stdc++.h>
#define ll long long
using namespace std;

void Effective_Approach()
{  ll array_size;
   cin>>array_size;
   ll array[array_size];
   map<ll,vector<ll>> position;
   for(int i = 0;i < array_size;i++)
   {   cin>>array[i];
       vector<ll> v;
       v.push_back(i+1); 
       v.push_back(array_size-i); 
       position[array[i]] = v;
   }
   int total_queries;
   ll total_search_from_start = 0,total_search_from_end = 0;
   cin>>total_queries;
   ll queries[total_queries];
   for(int i = 0;i < total_queries;i++)
   {   cin>>queries[i];
       total_search_from_start += position[queries[i]][0];
       total_search_from_end += position[queries[i]][1];
       
   }
   cout<<total_search_from_start<<" "<<total_search_from_end<<"\n";
   
       
    
}


int main() {
	int remained_test_cases = 1 ;
// 	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   Effective_Approach();
	    remained_test_cases--;
	}
	return 0;
}
