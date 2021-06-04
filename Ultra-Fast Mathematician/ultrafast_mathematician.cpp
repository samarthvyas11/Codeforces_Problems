#include <iostream>
#define ll long long
using namespace std;

string UltraFast_Mathematician() 
{   string number1,number2;
    cin>>number1>>number2;
    
    string output = "";
    for(int i = 0;i < number1.length();i++)
    {
        if(number1[i] == number2[i])
          output += "0";
        else
          output += "1";
          
    }
    
   return output;
}
int main() {
	int remained_test_cases = 1 ;
// 	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   cout<<UltraFast_Mathematician();
	    
	    remained_test_cases--;
	}
	return 0;
}
