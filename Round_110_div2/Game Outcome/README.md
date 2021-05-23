# Question:- Problem A)  Game Outcome 

# Link:-
   
   https://codeforces.com/contest/157/problem/A

# Time complexity :- O(N^2)

# Explanation :-
   
    As we can see that if we directly apply brute force we calculate the sum of each row or coloumns many times
so to avoid that we can initially store the summation of each coloumn and row for our future use ,
to acheive this create an array of N size for row and as well as for cloumn (matrix is of N*N) and intitalize 
each index with value 0. 
Now travel the whole matrix once and add that index value to the index of that row and coloumn in our 
arrays (array for storing summation)
Now as we have the data of sum of each row and coloumn ,iterate each index of matrix and check the condition(using our calculated data) 
if satisfied add it to answer .

