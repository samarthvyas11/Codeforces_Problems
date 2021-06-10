#include <bits/stdc++.h>
#define ll long long
using namespace std;

ll Number_of_pairs()
{ ll N,L,R;
  cin>>N>>L>>R;
  ll array[N];
  ll count_less_than_R = 0;
  for(ll i = 0;i<N;i++)
    { cin>>array[i];
      if(array[i]<R)
      count_less_than_R++; }
  ll arr_less_than_R[count_less_than_R];
  
  ll j = 0;
  for(ll i = 0;i<N;i++)
    { 
      if(array[i]<R)
      {arr_less_than_R[j] = array[i];
       j++;
      } 
        
    }
   ll len = count_less_than_R;
   sort(arr_less_than_R, arr_less_than_R + len);
   ll pairs_possible = 0;
   for(ll i = 0;i<len-1;i++)
   {
       if(arr_less_than_R[i] >= L)
       {
           ll start_at,lower,upper,find,mid;
           start_at = i + 1;
           lower = start_at;
           upper = len - 1 ;
           find = R - arr_less_than_R[i];
           
           if((arr_less_than_R[i] + arr_less_than_R[start_at]) <= R)
           {  
               while(lower < upper)
               { mid = (lower+upper+1) / 2;
               if(arr_less_than_R[mid]<=find)
                  lower = mid;
               else
                  upper = mid - 1;}
               pairs_possible += max(lower - start_at + 1,0ll); 
            //   cout<<"1 "<<pairs_possible<<"\n";
                   
               
           }
           
           
       }
       
       else{
           if(arr_less_than_R[i]+arr_less_than_R[len-1] >= L)
           { ll find,lower,upper,mid;
            find = L - arr_less_than_R[i];
            lower = i+1;
            upper = len - 1 ;
            while (lower < upper)
            {
                mid = (lower+upper)/2;
                if (arr_less_than_R[mid] >= find)
                    upper = mid;
                else
                   lower = mid+1;
                   
                
            }
            ll start_at = lower;
            lower = start_at;
            upper = len - 1,mid;
            find = R - arr_less_than_R[i];
            if(arr_less_than_R[i] + arr_less_than_R[start_at] <= R)
             {  while(lower < upper )
               {  mid = (lower + upper + 1)/2;
                 if (arr_less_than_R[mid] <= find)
                     lower = mid;
                 else
                    upper = mid - 1;
               }
               pairs_possible += max(lower - start_at + 1,0ll);
            //   cout<<"2 "<<pairs_possible<<"/n";
             }
           }
       }
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
