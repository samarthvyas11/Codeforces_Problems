# Question :- 
Problem C)  Intense Heat


# Link :-
https://codeforces.com/contest/1003/problem/C

# Time Complexity :- O(N^2)

# Explanation:-

Here the idea is brute force but in an efficient manner, for every temperature 
we travel all the temperature which are after it and consider it subtemp at every new index
and calculate its avg, in this way we calculate max avg;

pseudo code:-
avg = 0
for temp in temperature:
   sum = temp
   for temp1 in range(temp+1,temperature):
     sum += temp1
     if (temp1 - temp + 1) >= days condition:
              avg_of_this = sum / temp1-temp+1
              avg = max(avg,avg_of_this) 
         