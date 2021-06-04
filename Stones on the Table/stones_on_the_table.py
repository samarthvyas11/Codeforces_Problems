def Stones_on_the_Table():
    
    total_stones = int(input())
    color_of_stone = input()
    stones_remain_in_row = 1 
    prev_stone = color_of_stone[0]
    
    for st in range(1,total_stones):
        if color_of_stone[st] != prev_stone:
            stones_remain_in_row += 1 
            prev_stone = color_of_stone[st]
            
    return total_stones - stones_remain_in_row        
    
            
    
    
remained_test_cases = 1 
# remained_test_cases = int(input())
while remained_test_cases > 0:
    print(Stones_on_the_Table())
    remained_test_cases -= 1 