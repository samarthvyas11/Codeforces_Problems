def Number_of_pairs():
    N,L,R = map(int,input().split())
    arr = list(map(int,input().split()))
    array_lessthan_R = []
    
    for i in range(N):
        if arr[i] < R:
            array_lessthan_R.append(arr[i])
    possible_pairs = 0 
    array_lessthan_R.sort()
    
    for i in range(len(array_lessthan_R)-1):
        if array_lessthan_R[i] >= L:
            starts_at = i + 1
            lower = starts_at
            upper = len(array_lessthan_R) - 1
            f1 = R - array_lessthan_R[i]
            if array_lessthan_R[i] + array_lessthan_R[starts_at] <= R:
                while lower < upper:
                    mid = (lower + upper + 1) // 2 
                    if array_lessthan_R[mid] <= f1:
                        lower = mid 
                    else:
                        upper = mid - 1 
                possible_pairs += lower - starts_at + 1 
            
            
        else:
            if array_lessthan_R[i] + array_lessthan_R[-1] >= L :
                f1 = L - array_lessthan_R[i]
                lower = i+1
                upper = len(array_lessthan_R)-1
                while lower < upper:
                    mid = (lower + upper) // 2 
                    if array_lessthan_R[mid] >= f1:
                        upper = mid 
                    else:
                        lower = mid + 1 
                starts_at = lower
                lower = starts_at 
                upper = len(array_lessthan_R)-1 
                f1 = R - array_lessthan_R[i]
                if array_lessthan_R[i] + array_lessthan_R[starts_at] <= R:
                    while lower < upper:
                        mid = (lower + upper + 1) // 2 
                        if array_lessthan_R[mid] <= f1:
                            lower = mid 
                        else:
                            upper = mid - 1 
                    possible_pairs += lower - starts_at + 1        
        

                
                
                        
            
                
    return possible_pairs        
        
remained_test_cases = 1 
remained_test_cases = int(input())
while remained_test_cases > 0:
    print(Number_of_pairs())
    remained_test_cases -= 1 