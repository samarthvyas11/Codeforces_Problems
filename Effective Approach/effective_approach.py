def Effective_Approach():
    total_elements = int(input())
    array = list(map(int,input().split()))
    total_queries = int(input())
    position = {}
    
    for num in range(total_elements):
        position[array[num]] = [num+1,total_elements-num]
        
    total_check_from_start = 0
    total_check_from_end = 0
    
    queries = list(map(int,input().split()))
    for q in range(total_queries):
        total_check_from_start += position[queries[q]][0]
        total_check_from_end += position[queries[q]][1]
        
    return [total_check_from_start,total_check_from_end]    
        
    
remained_test_cases = 1 
# remained_test_cases = int(input())
while remained_test_cases > 0:
    print(*Effective_Approach())
    remained_test_cases -= 1 