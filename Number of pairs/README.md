# Question 
Number of Pairs

# Link:-
https://codeforces.com/contest/1538/problem/C

# Time Complexity: O(Nlog(N))

# Explanation :-
In step 1 lets change the array in such a way that it contains only numbers which are less than R;(we dont need number which are greater than R because they dont make any pair)
Now sort the array,
For every number from index 1 to index N-1(length of array - 1):-
 check whether number is greater than L :
 
 if greater than L:
     Get the rightmost index of number whose sum with this number is less than or equal to R ;(the numbers which are in betwwen this two will surely make pair with the present number)
     Inorder to acheive this use Binary search (lowest bound); // see code for clear understanding
       
 else:
  Get the nearest index of number on rightside of the number whose sum with this number is greater than equal to L;
  consider it as a start point 
  Again get the rightmost index of the number whose sum with this number is less than or equal to R;
 (The numbers which are in between start Point and this index will surely make pair with this number)
     
     
     
     
 
