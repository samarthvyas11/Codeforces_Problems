#include <bits/stdc++.h>
#define ll long long
using namespace std;

int Stone_Game()
{
    int total_stones;
    cin>>total_stones;
    int stones[total_stones],max_of_stones = 0,min_of_stones = 101;
    for(int i = 0;i < total_stones ;i++)
    {cin>>stones[i];
    max_of_stones = max(max_of_stones,stones[i]);
    min_of_stones = min(min_of_stones,stones[i]);
    }
    
    int min_index,max_index;
    for(int i = 0;i<total_stones;i++)
    { if(stones[i] == min_of_stones)
      min_index = i;
      if(stones[i] == max_of_stones)
      max_index = i;
    }
    
    int minimum_steps = min(max(max_index,min_index)+1,total_stones - min(min_index,max_index));
    int left_right = min(max_index,min_index)+1;
    left_right += total_stones - max(min_index,max_index);
    return min(minimum_steps,left_right);
    
}


int main() {
	int remained_test_cases = 1 ;
	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   cout<<Stone_Game()<<"\n";
	    remained_test_cases--;
	}
	return 0;
}
