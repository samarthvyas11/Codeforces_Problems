def question1():
    N = int(input())
    array = list(map(int,input().split()))
    min_of_arr = min(array)
    count_remove = 0 
    for i in range(N):
        if array[i] != min_of_arr:
            count_remove += 1 
    return count_remove        
remained_test_cases = int(input())
while remained_test_cases > 0:
    print(question1())
    remained_test_cases -= 1