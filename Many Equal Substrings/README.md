# Question:
Many Equal Substrings

# Link:
https://codeforces.com/contest/1029/problem/A

# Time complexity: O(N*N)

# Explanation:-
Search the maximum size substring which is formed by deleting 
characters only from left side and equal to the string which is formed as:- starts from starting of original string
and equal to its (the substring we found) length
i,e' abab :- substring is 'ab' (start from index 3)
so this part is common, add the remaing part(string without founded substring) to (K-1) times to the original string to get the output. 