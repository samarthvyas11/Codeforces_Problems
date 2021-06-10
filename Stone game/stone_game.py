def Stone_Game():
    N = int(input())
    stones = list(map(int,input().split()))
    max_of_stones = max(stones)
    min_of_stones = min(stones)
    
    max_index = stones.index(max_of_stones) 
    min_index = stones.index(min_of_stones)
    left_right = min(max_index,min_index)+1  # minimum from left side
    left_right += N - max(max_index,min_index) # maximum from right side
    
    return min(max(max_index,min_index)+1,max(N - max_index,N - min_index),left_right)
 
        
remained_test_cases = 1 
remained_test_cases = int(input())
while remained_test_cases > 0:
    print(Stone_Game())
    remained_test_cases -= 1 