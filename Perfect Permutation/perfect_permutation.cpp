#include <iostream>
#define ll long long
using namespace std;

void Perfect_Permutation() 
{   int permutation;
    cin>>permutation;
    int per[permutation];
    
    
    for(int i = 0;i < permutation;i++)
    {
        per[i] = i+1;
    }
    
    if(permutation % 2 == 1)
    {   cout<<-1<<"\n";
        return ;
        
    }
       
    int i = 0;
    while (i+1 < permutation)
    { int c;
      c = per[i];
      per[i] = per[i+1];
      per[i+1] = c;
      i = i + 2  ;  
    }
    
    for(int i = 0 ;i < permutation ;i++)
     cout<<per[i]<<" ";
     
    return ; 
}
int main() {
	int remained_test_cases = 1 ;
// 	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   Perfect_Permutation();
	    remained_test_cases--;
	}
	return 0;
}
