# Question :- 
 Little Alawn's Puzzle

# Link:-
https://codeforces.com/contest/1534/problem/C

# Time complexity :- O(N)

# Explanation:- 

In it we have to find the groups of pairs such that in one group each pair have to be swapped to
fullfill the condition.

In order to find the group visit each index and if it is not visited(keep a "done" name array which keeps the record that this index is visited or not )
start counting pairs for that,(count pairs until we get the number on array1 as equal value of the taken index of array2)
Visit code to understand better.




Our answer is 2^groups % 1000000007
