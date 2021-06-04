def Nearly_Lucky_Number():
    number = int(input())
    count_lucky_number = 0
    
    while number > 0:
        digit = number % 10
        if digit == 4 or digit == 7:    #lucky numbers are 4 and 7
            count_lucky_number += 1
        number = number // 10 
    if count_lucky_number == 4 or count_lucky_number == 7:
        return True
    return False    
            
    
    
remained_test_cases = 1 
# remained_test_cases = int(input())
while remained_test_cases > 0:
    if (Nearly_Lucky_Number()):
        print("YES")
    else:
        print("NO")
    remained_test_cases -= 1 