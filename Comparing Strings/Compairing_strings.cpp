#include <bits/stdc++.h>
#define ll long long
using namespace std;


string Comparing_Strings()
{ string str1,str2;
  cin>>str1;
  cin>>str2;
  ll not_same = 0;
  if (str1.length() != str2.length())
      return("NO");
  vector<ll> index_not_same;
  
  for(int i = 0 ;i < str1.length();i++)
  {
      if(str1[i] != str2[i])
      {
          not_same++;
          index_not_same.push_back(i);
      }
  }
  
  if(not_same != 2)
     return ("NO");
     
  char temp = str1[index_not_same[0]];
  str1[index_not_same[0]] = str1[index_not_same[1]];
  str1[index_not_same[1]] = temp;
  
  if(str1 != str2)
      return  ("NO");
  
  
  return ("YES");

}


int main() {
	int remained_test_cases = 1 ;
// 	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   cout<<Comparing_Strings()<<"\n";
	    remained_test_cases--;
	}
	return 0;
}
