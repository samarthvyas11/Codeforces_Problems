# Question:
Problem C Alphabetic Removals
# Link:
https://codeforces.com/contest/999/problem/C




# Time complextity:O(N+26) => O(N)

# Explanation:
Basically the idea to find the solution is that ,
start removing alphabet according to their lexagraphical 
order (number of times given in the question) (as per their availability)

To acheive above idea:-

While travelling the original string count the number of 
times an alphabet is present ,in this code I used a 26 size 
list to store the count of 26 (lower alphabets) alphabets.


Then travel this 26-length array and calculate that how many times we have to 
remove that alphabet (if the count of that alphabet is greater than desired remove
remove all occurence of this alphabet or if it is less than then remove the 
remained desired remove)

