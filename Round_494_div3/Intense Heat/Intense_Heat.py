# from collections import Counter
def question3():


    days,min_cons_days = map(int,input().split())
    temperature_per_day = list(map(int,input().split()))
    max_avg = 0 


    for start_day in range(days-min_cons_days+1):
        at_day = start_day
        sum_temps = 0
        while at_day < days:
            sum_temps += temperature_per_day[at_day]
            if (at_day - start_day + 1) >= min_cons_days:
                max_avg = max(max_avg,sum_temps/(at_day-start_day+1))
            at_day += 1 
            

    return max_avg
    
           
            
  

# remained_test_cases = int(input())
remained_test_cases = 1 
while remained_test_cases > 0:
    print(question3())
    remained_test_cases -= 1 