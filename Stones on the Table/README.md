# Question:-
Stones on the Table

# Link :-
https://codeforces.com/problemset/problem/266/A

# Time complexity:- O(N)

# Explanation :- 
 Follow Greedy Approach:
  store first color as previous color 
Start itterating the colors from index 2
if color is different from previous color 
include it in the final row count and change previous color to 
this color.


we get the final row count as the remaining color in the row,
for output :- total_color - final row count 
