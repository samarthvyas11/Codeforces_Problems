# Question 
 Arrival of the General

# Link :-
  https://codeforces.com/problemset/problem/144/A

# Time Complexity:- O(N)

# Explanation:- 

As we have to focus on the maximum number index from left side(if more than one then select left most) ,
and minimum number index from right side(if more than one then select right most);

if max index is less than min index i.e, they wil not meet in swaping
so answer is max index + (total soldiers - min index)
else
 max index + ( total soldiers - min index) - 1 (there is one swap which is common in both)


Note : - Indexing starts from 1 