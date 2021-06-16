def power(x,y):
    MOD = 1000000007
    res = 1 
    x = x % MOD
    while y > 0:
        if y & 1:
            res = (res*x) % MOD
        y = y>>1 
        x = (x*x) % MOD
        
    return res    
    

def Plant():
    years = int(input())
    if years == 0:
        return 1
    return (power(2,(years-1)) + power(2,(2*years) - 1)) % 1000000007
    
    
remained_test_cases = 1 
# remained_test_cases = int(input())
while remained_test_cases > 0:
    print(Plant())
    remained_test_cases -= 1 