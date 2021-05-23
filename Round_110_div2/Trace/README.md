# Question Problem B) Trace

# Link:- https://codeforces.com/contest/157/problem/B

# Time complexity :- O(N log(N))

# Explanation:-

It is given that the color outside the concentric circles are blue , so 
we conlclude that the outermost circle must have red in color and then 
alternate blue - red - blue pattern will be followed.

So as per the pattern calculate the area of the circles with red color:-

  1) Sort the radius in decreasing order
  2) Iterate each radius from largest to smallest
      If atleast one radius is remaing after the current radius 
         red_area += pie*(current_radius^2 - next_radius^2)
      else
          red_area += pie*(current_radius^2)

