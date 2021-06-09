# Question:
Common Divisors

# Link:-
https://codeforces.com/contest/182/problem/D

# Time Complexity:- O(N*N)

# Explanation:-
First we have to calculate the substrings which are the divisors of the main string for 
both the string  :-
        To acheive this we first calculate the factors of the length of the string,
        then itterating that factors:
             Find whether the sub_string with length equal to factor (string[0 to factors[i]])is a
             divisor of the string or not,

Now we have two list of substrings which are the dvivisors of the string respectively,
Count common divisors in both the lists,that is our answer.    
