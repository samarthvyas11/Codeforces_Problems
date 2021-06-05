def Perfect_Permutation():
    permutation = int(input())
    per = [i for i in range(1,permutation+1)]
    
    if permutation % 2 == 1:
        return [-1]
    
    i = 0 
    while i+1 < permutation:
        
        per[i],per[i+1] = per[i+1],per[i]
        i += 2
        
        
    return per    
           
    
    

remained_test_cases = 1 
# remained_test_cases = int(input())
while remained_test_cases > 0:
    print(*Perfect_Permutation())
    remained_test_cases -= 1 