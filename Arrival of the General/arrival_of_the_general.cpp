#include <iostream>
#define ll long long
using namespace std;

int Arrival_of_the_General()
{   int soldiers_count;
    cin>>soldiers_count;
    int height_of_soldier[soldiers_count];
    
    for(int i = 0 ;i < soldiers_count ;i++)
    {cin>>height_of_soldier[i];}
    
    int max_height = height_of_soldier[0];
    int max_height_index = 0;
    int min_height = height_of_soldier[0];
    int min_height_index = 0;
    
    for(int soldier = 1 ;soldier < soldiers_count ;soldier++)
    {
        if(height_of_soldier[soldier] > max_height)
        {   max_height = height_of_soldier[soldier];
            max_height_index = soldier;
        }
        
        if(height_of_soldier[soldier] <= min_height )
        {
            min_height = height_of_soldier[soldier];
            min_height_index = soldier;
        }
    }
    
    
    if(max_height_index < min_height_index)
    return(max_height_index + (soldiers_count - 1 - min_height_index));
    
    return (max_height_index + (soldiers_count - 1 - min_height_index ) - 1);
    
    
}


int main() {
	int remained_test_cases = 1 ;
// 	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   cout<<Arrival_of_the_General();
	    remained_test_cases--;
	}
	return 0;
}
