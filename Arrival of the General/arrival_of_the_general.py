def Arrival_of_the_General():
    soldiers_count = int(input())
    height_of_soldier = list(map(int,input().split()))
    max_height = height_of_soldier[0]
    max_at_index = 0
    min_height = height_of_soldier[0]
    min_at_index = 0
    
    for i in range(1,soldiers_count):
        if height_of_soldier[i] > max_height:
            max_height = height_of_soldier[i]
            max_at_index = i 
            
        if height_of_soldier[i] <= min_height:
            min_height = height_of_soldier[i]
            min_at_index = i 
    
    if max_at_index < min_at_index:
        return max_at_index + (soldiers_count - 1 - min_at_index)
        
    return max_at_index + (soldiers_count - 1 - min_at_index) - 1     
    
    

remained_test_cases = 1 
# remained_test_cases = int(input())
while remained_test_cases > 0:
    print(Arrival_of_the_General())
    remained_test_cases -= 1 