# Question :- 
Problem B) Sifid and Strange Subsequences

# Link:-
https://codeforces.com/contest/1529/problem/B

# Time Complexity: O(Nlog(N))

# Explanation:-

Lets us think that if we have a sequence of all negative numbers then the absolute difference of any two value must be zero or any positive integer,so our
subsequence should include all the negative numbers , as the absolute difference of any two is surely greater than or equal to zero which is 
greater than maximum value of subsequence which is negative,

So till now we conclude that we should include all the negative numbers in our subsequence,as if there is a positive number which is less than or equal 
to the minimum difference from pair of negative numbers then we can also consider that positive number in our subsequence, but atmost 1 positive integer because
the difference of positive integer is always less than the maximum of them.

