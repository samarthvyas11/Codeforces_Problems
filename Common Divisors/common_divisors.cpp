#include <bits/stdc++.h>
#define ll long long
using namespace std;

vector<string> check_repeated(string s)
{
    ll len = s.length();
    vector<int> factors;
    vector<string> repeated;
    for(ll i = 1 ;i <= len;i++ )
    {
        if(len % i == 0)
        factors.push_back(i);
    }
    
    for (auto i = factors.begin(); i != factors.end(); ++i)
    {   string s1 = "";
        for(int j = 0 ;j < *i ;j++ )
         s1 += s[j];
        bool found = true; 
        ll j = *i ;
        while (j < len)
        {   string s2 = "";
            for(int z = j;z < j + *i;z++)
              s2 += s[z];
              
            if(s1 != s2)
            {
                found = false;
                break;
            }
              
            j += *i ;
        }
        
        if(found)
        repeated.push_back(s1);
         
    }
    return (repeated);
    
    
    
}

int Common_Divisors()
{ string first,second;
  cin>>first>>second;
  vector<string> repeated_first = check_repeated(first);
  vector<string> repeated_second = check_repeated(second);
  ll common_divisors = 0;
  
  
  for(auto i = repeated_first.begin();i != repeated_first.end();++i)
  {for(auto j = repeated_second.begin();j != repeated_second.end();++j)
       {if(*i == *j)
           { common_divisors++;
               break;
           }
       }
  }
  return (common_divisors);
  
  
  
  
}


int main() {
	int remained_test_cases = 1 ;
// 	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   cout<<Common_Divisors();
	    remained_test_cases--;
	}
	return 0;
}
