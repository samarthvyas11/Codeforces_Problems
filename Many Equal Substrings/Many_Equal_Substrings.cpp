#include <bits/stdc++.h>
#define ll long long
using namespace std;
string string_upto(string str,int start,int end)
{
    string output = "";
    for(int i = start;i <= end ; i++)
     output += str[i];
    return (output); 
}

string Many_Equal_Substrings()
{  ll N,times;
   cin>>N>>times;
   string main_str;
   cin>>main_str;
   ll max_same_from = 0;
   
   ll word = 1;
   while(word < N)
   {
       if(string_upto(main_str,word,N-1) == string_upto(main_str,0,N-word-1))
        { max_same_from = N - word;
          break;}
        word++;  
       
   }
   string output = main_str;
   string add =  string_upto(main_str,max_same_from,N-1);
   for(int i = 0;i< times-1;i++)
       output += add;
   return (output);
   
   
   
}


int main() {
	int remained_test_cases = 1 ;
// 	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   cout<<Many_Equal_Substrings()<<"\n";
	    remained_test_cases--;
	}
	return 0;
}
