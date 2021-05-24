# Question :- 
Problem A) Eshag Loves Big Arrays

# Link:-
https://codeforces.com/contest/1529/problem/A

# Time Complexity :- O(N)

# Explanation:-

In order to acheive the goal ,we need to find the times the min(array) (minumum number of the array) present in the array.
Because if we pair two numbers which are not equal then surely one number is greater then their average, so in our array
to delete maximum numbers we make a subsequence of two numbers each time where one number is the minimum number of the array
and other is the remaining elements of the array, as a outcome the only numbers which remains are the numbers which are equal to minimum
number of the array .
So our answer is ( Length of array - count of min(array) in array )



