#include <bits/stdc++.h>
#define ll long long
using namespace std;

int Jzzhu_and_Children()
{ ll total_students,chocolates_per_day;
  cin>>total_students>>chocolates_per_day;
  ll chocolates_required[total_students];
  ll in_step[total_students],max1 = -1 ;
  
  for(int i = 0;i < total_students;i++)
  {   cin>>chocolates_required[i];
      float times = float(chocolates_required[i]) / chocolates_per_day;
      in_step[i] = ceil(times);
      max1 = max(max1,in_step[i]);
      
  }
  ll length = total_students - 1 ;
  
 

  while (length >= 0)
  {  if(in_step[length] == max1)
       return (length + 1) ;
     length--; 
  }
   
   
}


int main() {
	int remained_test_cases = 1 ;
// 	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   cout<<Jzzhu_and_Children();
	    remained_test_cases--;
	}
	return 0;
}
