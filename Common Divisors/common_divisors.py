def check_repeatation(string):
    l1 = len(string)
    factors = []
    for i in range(1,l1+1):
        if l1 % i == 0:
            factors.append(i)
    repeated = []        
    for i in range(len(factors)):
        found = True
        s1 = string[:factors[i]]
        j = factors[i]
        while j < l1:
            s2 = string[j:j+factors[i]]
            j += factors[i]
            if s1 != s2:
                found = False
                break 
        if found:
            repeated.append(s1)
            
    return repeated        
            
        
        


def Common_Divisors():
    stirng1 = input()
    string2 = input()
    s1_repeated = check_repeatation(stirng1)
    s2_repeated = check_repeatation(string2)
    
    common_divisor = 0 
    for i in range(len(s1_repeated)):
        if s1_repeated[i] in s2_repeated:
            common_divisor += 1 
    return common_divisor        
            
        
remained_test_cases = 1 
# remained_test_cases = int(input())
while remained_test_cases > 0:
    print(Common_Divisors())
    remained_test_cases -= 1 