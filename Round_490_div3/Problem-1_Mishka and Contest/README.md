# Question:- 
Problem 1)   Mishka and Contest
# Link :-
https://codeforces.com/contest/999/problem/A



# Time Complexity :- O(N)

# Explanation :-

As a step-1 we have to travel from left side  and check the
diffculty level of questions, here any one of the two conditions 
should occur

1) We will get difficulty level greater than  skill at that index
break the itterations(count questions upto this index-1)


2)None of the given questions have difficulty level greater then skill level

If condition one happend than travel the list from right 
and break when any question have difficulty level greater then skill(which will surely happen) and count question upto this index from right(count-1)(as the current question 
is not acceptable)
Total count is our answer

If condition two happend than total number of questions is our answer





 
