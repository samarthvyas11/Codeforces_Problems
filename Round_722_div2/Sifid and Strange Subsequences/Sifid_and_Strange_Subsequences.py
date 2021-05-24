def question2():
    N = int(input())
    arr = list(map(int,input().split()))
    neg = []
    pos = []

    for i in range(N):
        if arr[i] <= 0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])

    if len(neg) == N:
        return N

    if len(neg) == 0:
        return 1

    neg.sort()

    min_diff = float('inf')
    for i in range(len(neg)-1):
        min_diff = min(min_diff,abs(neg[i]-neg[i+1]))

    max = 0     
    for i in range(len(pos)):
        if pos[i] <= min_diff:
            return len(neg) + 1

    return len(neg)        
        
        
remained_test_cases = int(input())
while remained_test_cases > 0:
    print(question2())
    remained_test_cases -= 1 