def power_of(N):
    if N == 0:
        return 1 
    elif N == 1:
        return 2 
    else:
        return (power_of(N//2)*(power_of(N - (N//2)))) 
def Little_Alawns_Puzzle():
    N = int(input())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    done = [False for i in range(N)]
    index1 = [0 for i in range(N)]
    index2 = [0 for i in range(N)]

    for i in range(N):
        index1[arr1[i]-1] = i 
        index2[arr2[i]-1] = i

    count_pair = 0 
    count_done = 0
    for i in range(N):
        if not done[i]:
            at_index= i
            while arr1[at_index] != arr2[i]:
                done[at_index] = True
                count_done += 1 
                at_index = index2[arr1[at_index]-1]
            done[at_index] = True
            count_done += 1
            count_pair += 1             
        
    
    
    return power_of(count_pair) % 1000000007  
            
    

remained_test_cases = 1 
remained_test_cases = int(input())
while remained_test_cases  > 0:
    print(Little_Alawns_Puzzle())
    remained_test_cases -= 1 
    