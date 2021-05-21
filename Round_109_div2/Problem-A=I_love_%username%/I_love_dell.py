def question1():
    
    competition_count = int(input())
    points_in_comp = list(map(int,input().split()))
    max_min_count = 0
    max_point = points_in_comp[0]
    min_point = points_in_comp[0]
    
    for point in range(1,competition_count):
        if points_in_comp[point] < min_point:
            max_min_count += 1 
            min_point = points_in_comp[point]
        if points_in_comp[point] > max_point:
            max_min_count += 1 
            max_point = points_in_comp[point]
    return max_min_count        
        
        
    
# remained_test_cases = int(input())
remained_test_cases = 1 
while remained_test_cases > 0 :
    print(question1())
    remained_test_cases -= 1 