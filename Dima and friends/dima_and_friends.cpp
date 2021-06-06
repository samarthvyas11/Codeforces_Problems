#include <bits/stdc++.h>
#define ll long long
using namespace std;

int Dima_and_Friends()
{  ll total_friends;
   cin>>total_friends;
   ll value_shown_by_friend[total_friends];
   ll total_moves = 0;
   
   for(int i = 0;i < total_friends;i++)
   {   cin>>value_shown_by_friend[i];
       total_moves += value_shown_by_friend[i];
   }
   
   ll total_people = total_friends + 1 ; //her friend and she 
   int posible_ways = 0;
   if ((total_moves + 1) % total_people != 1)
       posible_ways++;
    if ((total_moves + 2) % total_people != 1)
       posible_ways++;
    if ((total_moves + 3) % total_people != 1)
       posible_ways++;
    if ((total_moves + 4) % total_people != 1)
        posible_ways++;
    if ((total_moves + 5) % total_people != 1)
       posible_ways++;
       
       
    return (posible_ways);   
   
   
   
}


int main() {
	int remained_test_cases = 1 ;
// 	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   cout<<Dima_and_Friends();
	    remained_test_cases--;
	}
	return 0;
}
