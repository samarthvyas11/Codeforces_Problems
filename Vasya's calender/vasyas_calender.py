def Vasyas_Calendar():
    days_limit = int(input())
    months = int(input())
    days_in_month = list(map(int,input().split()))
    ongoing_day = days_in_month[0] + 1 
    
    if days_in_month[0] == days_limit:
        ongoing_day = 1 
    increase = 0    
    
    for m in range(1,months):
        if ongoing_day != 1:
            # print("ongoing_day",ongoing_day)
            increase += days_limit + 1 - ongoing_day 
            # print(days_limit + 1 - ongoing_day)
            ongoing_day = 1 
        ongoing_day += days_in_month[m]  
    
    return increase    
            
            
        
remained_test_cases = 1 
# remained_test_cases = int(input())
while remained_test_cases > 0:
    print( Vasyas_Calendar())
    remained_test_cases -= 1 