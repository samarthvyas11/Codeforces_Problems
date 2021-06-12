def Creating_the_Contest():
  total_problems = int(input())
  diff_of_prob = list(map(int,input().split()))
  max_subset_len = 1
  count_satisfied = 0
  
  for i in range(total_problems-1):
      if diff_of_prob[i+1] <= 2*diff_of_prob[i]:
          count_satisfied += 1 
      else:
          max_subset_len = max(max_subset_len,count_satisfied+1)
          count_satisfied = 0
          
  max_subset_len = max(count_satisfied+1,max_subset_len)
  return max_subset_len
      
       
       
            
reamined_test_cases = 1         
# reamined_test_cases = int(input())
while reamined_test_cases > 0:
    print(Creating_the_Contest())
    reamined_test_cases -= 1 
