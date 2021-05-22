# Question:- 
Problem-B Combination
# Link :-
https://codeforces.com/contest/155/problem/B

# Time Complexity:- O(N^2)

# Explanation:-
In this problem Firstly Copy the set of values (A,B) to two arrays
(sort_accord_top,sot_accord_down), sort the first one with the values 
that are at index 0 in it and second with value at index 1.

As we are initially having the chances that remain to select a card is one ,
The priority is given in this way:-


The priority is 
given to the card which has highest number on the top (In our array it is at the last position of the sort_accord_top)
if the remained_chance is 1 then prority is given to the card which has highest value on bottom
(In ourr array last element of sort_accord_down).

As all the cards are taken or remained_chances become zero ,we get our answer.



In code max_score is the output. 

 

