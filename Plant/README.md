# Question 
Plant

# Link:-
https://codeforces.com/contest/186/problem/C

# Time Complexity :- O(Nlog(N))

# Explanation:-
Let us conside "X" be the triangle facing upwards and "Y" be the traingle facing downwards
So in particular year we can say that,
                                      X + Y = 4^years   ---------(1)
                                     and                              
                                      X - Y = 2^years    ---------(2)
                  
                 Applying,elimination method over 1 and 2,
                 we get,     => 2*X = 4^years + 2^years
                             => 2*X = 2^(2*years) + 2^years
                             =>   X = 2^(2*years - 1) + 2^(years - 1)     (Answer)
                    