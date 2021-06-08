#include <bits/stdc++.h>
#define ll long long
using namespace std;

void Present_from_lena()
{ int N;
  cin>>N;
  
  //UPPER HALF
  for(int i = 0;i <= N ;i++ )
  {
      for(int j = i ;j < N;j++ )
      cout<<" "<<" ";
      if (i == 0)
         cout<<0;
      else{
         for(int j = 0;j <= i;j++)
            
              cout<<j<<" ";
      } 
      
      int j = i - 1 ;
      while (j >= 0)
      { if(j == 0)
         cout<<j;
        else 
          cout<<j<<" ";
          j -= 1;
          
      }
      cout<<"\n";
      
      
  }
  // LOWER HALF
  for(int i = 0 ;i < N ;i++)
  {
      for(int j = 0;j <= i;j++)
         cout<<"  ";
      if(i == N-1)
      cout<<0;
      else
      {
          for(int j = 0 ;j < N - i;j++)
          cout<<j<<" ";
      }
      int j = N - i - 2;
      while(j>=0)
      {if(j == 0)
       cout<<0;
       else
          cout<<j<<" ";
          j -= 1;
      }
      cout<<"\n";
      
      
      
  }
  
  
  
  
  
  
}


int main() {
	int remained_test_cases = 1 ;
// 	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   Present_from_lena();
	    remained_test_cases--;
	}
	return 0;
}
