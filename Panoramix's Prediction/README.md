# Question :
  Panoramix's Prediction

# Link :
https://codeforces.com/problemset/problem/80/A

# Time complexity :- O(N)

# Explanation :
As we can see that the range of n is small,
so instead of calculating next prime number
we,
can create an array by ourself which includes all the prime
numbers between 1 to 50 in ascending order,check the very next
number(in array) of the prime number given in the testcase if it is same
as next prime then output is yes else no 

If number is 47 then also it is "NO" because next prime number would be greater than 50
which is false for our case
 