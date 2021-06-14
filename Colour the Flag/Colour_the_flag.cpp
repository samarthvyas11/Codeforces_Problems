#include <bits/stdc++.h>
#define ll long long
using namespace std;
int Colour_the_Flag()
{ int row,col;
  cin>>row>>col;
  vector<string> grid;
  int count_dot = 0;

  for(int r = 0;r < row;r++)
  {  string c;
     cin>>c;
     count_dot += count(c.begin(), c.end(), '.');
     grid.push_back(c);
  }

  if(count_dot == row*col)
  grid[0][0] = 'R';

  for(int i = 0;i < 2;i++)
  {
      for(int r = 0;r < row;r++)
      {
          for(int c = 0;c < col;c++)
          { if(grid[r][c]  != '.')
            {   char next;
                int j;
                // Left 
                if(grid[r][c] == 'R')
                    next = 'W';
                else
                    next = 'R';
                j = c-1;
                while (j >= 0)
                {
                    if(grid[r][j] != '.')
                    {
                        if(grid[r][j] != next)
                        {    cout<<"NO"<<"\n";
                            return (0) ;}
                        else
                            break;
                    }
                    else
                    {grid[r][j] = next;
                     if(grid[r][j] == 'R')
                          next = 'W';
                     else
                         next = 'R';
                        
                    }
                    j -= 1;
                }
                
                
                // Right
                if(grid[r][c] == 'R')
                    next = 'W';
                else
                    next = 'R';
                j = c+1;
                while (j < col)
                {
                    if(grid[r][j] != '.')
                    {
                        if(grid[r][j] != next)
                         {   cout<<"NO"<<"\n";
                            return (0); }
                        else
                            break;
                    }
                    else
                    {grid[r][j] = next;
                     if(next == 'R')
                         next = 'W';
                     else
                         next = 'R';
                        
                    }
                    j += 1;
                }
                
                // top
                if(grid[r][c] == 'R')
                    next = 'W';
                else
                    next = 'R';
                j = r-1;
                while (j >= 0)
                {
                    if(grid[j][c] != '.')
                    {
                        if(grid[j][c] != next)
                          {  cout<<"NO"<<"\n";
                            return (0); }
                        else
                            break;
                    }
                    else
                    {grid[j][c] = next;
                     if(next == 'R')
                         next = 'W';
                     else
                         next = 'R';
                        
                    }
                    j -= 1;
                }
                
                // bottom
                
                if(grid[r][c] == 'R')
                    next = 'W';
                else
                    next = 'R';
                j = r+1;
                while (j < row)
                {
                    if(grid[j][c] != '.')
                    {
                        if(grid[j][c] != next)
                         {   cout<<"NO"<<"\n";
                            return(0) ;}
                         else
                            break;
                    }
                    else
                    {grid[j][c] = next;
                     if(next == 'R')
                         next = 'W';
                     else
                         next = 'R';
                        
                    }
                    j += 1;
                }
                
                
                
                
            }
              
          }
      }
      
      
      
      
      
      
  }
  cout<<"YES"<<"\n";
  for(int r = 0 ;r< row;r++)
  {
      for(int c = 0 ; c < col;c++)
       cout<<grid[r][c];
       cout<<"\n";
  }
  
  return 0;
  
  
  
  
}


int main() {
	int remained_test_cases = 1 ;
	cin>>remained_test_cases;
	while(remained_test_cases > 0)
	{   Colour_the_Flag();
	    remained_test_cases--;
	}
	return 0;
}
