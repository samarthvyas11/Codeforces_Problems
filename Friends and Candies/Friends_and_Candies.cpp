#include <bits/stdc++.h>
#define ll long long
using namespace std;

int Friends_and_Candies()
{
   ll total_friends;
   cin>>total_friends;
   ll candies_friend_have[total_friends];
   ll total_candies = 0;
   
   for(ll i = 0 ;i < total_friends; i++)
   {  cin>>candies_friend_have[i];
      total_candies += candies_friend_have[i];
       
   }
   
   if(total_candies % total_friends != 0)
   return -1;
   ll each_get = total_candies / total_friends;
   ll  minimum_select = 0;
   
   for(ll i = 0; i < total_friends ;i++ )
   {
       if(candies_friend_have[i] > each_get)
       minimum_select += 1 ;
   }
   
   return minimum_select;
   
   
}


int main() {
	int remained_test_cases = 1 ;
	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   cout<<Friends_and_Candies()<<"\n";
	    remained_test_cases--;
	}
	return 0;
}
