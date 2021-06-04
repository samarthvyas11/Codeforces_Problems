#include <iostream>
#define ll long long
using namespace std;

int Stones_on_the_Table()
{
    ll total_stone;
    cin>>total_stone;
    string color_of_stone;
    cin>>color_of_stone;
    ll stone_remain_in_row = 1;
    char prev = color_of_stone[0];
    for(int i = 1;i < total_stone;i++)
    {
        if(color_of_stone[i] != prev)
        {  stone_remain_in_row++;
           prev = color_of_stone[i] ;
        }
    }
    
    return (total_stone - stone_remain_in_row);

}
int main() {
	int remained_test_cases = 1 ;
// 	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   cout<<Stones_on_the_Table();
	    remained_test_cases--;
	}
	return 0;
}
