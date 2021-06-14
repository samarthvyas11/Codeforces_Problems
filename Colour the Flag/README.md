# Question :-
Colour the Flag

# Link:-
https://codeforces.com/contest/1534/problem/A

# Time complexity:- O(N*N)

# Explanation :- 
Initially we have to check whether there is any coloured box or not ,if there is no box which is coloured 
then coloured the first box with your choice,

Itterate the whhole grid,when you find a coloured box :-
 Travel left to it
 Travel right to it
 Travel top from  it
 Travel bottom from it
 

 Give alternate colour to each box , if any coloured box arrived in the path then check does it in order or not
(alternate or not ) if it is then break the loop ,otherwise return "NO"

we have to perform above steps two times because in worst case the above step will form one row and one coloumn 
in one step and whole grid in two steps.

If the value until now is not returned cout yes and print the grid