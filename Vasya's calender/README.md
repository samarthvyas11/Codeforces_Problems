# Questions : 
Vasya's Calender

# Link:-
https://codeforces.com/contest/182/problem/B

# Time complexity: O(N)

# Explanation :- 
Basically we have to check the on_going day on each first day
of the month ,if it is not equal to 1 then count the number of increments
required to make it 1 (ongoing day = 1,2,3,...day_limit,1,2....day_limit ...)


Pseudo code:
ongoing_day = 1 
increment = 0
for month = 1 ,month < month_limit ,month ++ 
    if ongoing_day != 1
       increment += day_limit - on_going_day + 1 
       ongoing_day = 1 
    ongoing_day += day_in_month[month]

return increment