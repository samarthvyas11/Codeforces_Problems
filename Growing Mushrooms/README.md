# Question 
Growing Mushrooms

# Link :- 
https://codeforces.com/contest/186/problem/B

# Time Comlexity :- O(NlogN)

# Explanation:-
Check both the cases for each planter (first slot with speed1 and second with speed2)
and (second slot with speed2 and first with speed1) and consider the case which gives maximum 
output.
Store each output with index  in a list  ([index,max_height]),
sort the list in decreasing order by taking second place as a key. 
