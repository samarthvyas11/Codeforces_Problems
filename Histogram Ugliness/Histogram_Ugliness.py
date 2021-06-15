def Histogram_Ugliness():

    total_bars = int(input())
    bars = list(map(int,input().split()))
    ugli = 0
    last = 0

    for i in range(total_bars):
        if bars[i] > last:
            ugli += bars[i] - last 
        last = bars[i]
        if i == total_bars - 1:
            ugli += bars[i]
            break
        if bars[i+1] < bars[i]:
            ugli += bars[i] - bars[i+1]
    if total_bars == 1:
        ugli -= bars[0]
        return ugli

    for i in range(total_bars):
        if i == 0:
            if bars[i+1] < bars[i]:
                ugli -= bars[i] - bars[i+1]
                bars[i] = bars[i+1]
            
        if i == total_bars-1:
            if bars[i-1] < bars[i]:
                ugli -= bars[i] - bars[i-1]
                bars[i] = bars[i-1]
            
        else:
            if bars[i] > bars[i-1] and bars[i] >  bars[i+1]:
                if bars[i-1] > bars[i+1]:
                    ugli -= (bars[i] - bars[i-1])
                    bars[i] = bars[i-1]
                else:
                    ugli -= (bars[i] - bars[i+1])
                    bars[i] = bars[i+1]
                
            
            
    return ugli  
            
        
remained_test_cases = 1 
remained_test_cases = int(input())

while remained_test_cases  > 0:
    print(Histogram_Ugliness())
    remained_test_cases -= 1 
    