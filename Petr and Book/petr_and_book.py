import math
def Petr_and_Book():
    total_pages_to_read = int(input())
    pages_on_day = list(map(int,input().split()))
    day = 0
    
    
    while total_pages_to_read > 0:
        total_pages_to_read -= pages_on_day[day]
        if total_pages_to_read <= 0:
            return day + 1 
        day += 1 
        if day == 7:
            day = 0 
        
    
    
remained_test_cases = 1 
# remained_test_cases = int(input())
while remained_test_cases > 0:
    print(Petr_and_Book())
    remained_test_cases -= 1 