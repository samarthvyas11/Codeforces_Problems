def find(N):
    
    if N < 10:
        return N 
    elif N <= 100 :
        if N == 100:
            return 3 + find(99)
        k1 = N // 10 
        rem = N % 10 
        return rem + 11*k1
    elif N <= 1000:
        if N == 1000:
            return 4 + find(999)
        k1 = N // 100 
        rem = N % 100 
        return find(rem) + find(100)*k1
    elif N <= 10000:
        if N == 10000:
            return 5 + find(9999)
        k1 = N // 1000 
        rem = N % 1000 
        return find(rem) + find(1000) * k1 
    elif N <= 100000:
        if N == 100000:
            return 6 + find(99999)
        k1 = N // 10000  
        rem = N % 10000  
        return find(rem) + find(10000) * k1
    elif N <= 1000000:
        if N == 1000000:
            return 7 + find(999999)
        k1 = N // 100000  
        rem = N % 100000  
        return find(rem) + find(100000) * k1
    elif N <= 10000000:
        if N == 10000000:
            return 8 + find(9999999)
        k1 = N // 1000000  
        rem = N % 1000000  
        return find(rem) + find(1000000) * k1
    elif N <= 100000000:
        if N == 100000000:
            return 9 + find(99999999)
        k1 = N // 10000000  
        rem = N % 10000000  
        return find(rem) + find(10000000) * k1
    elif N <= 1000000000:
        if N == 1000000000:
            return 10 + find(999999999)
        k1 = N // 100000000  
        rem = N % 100000000  
        return find(rem) + find(100000000)* k1    
    
def Interesting_Function():
    L,R = map(int,input().split())
    return find(R) - find(L)
            
reamined_test_cases = 1         
reamined_test_cases = int(input())
while reamined_test_cases > 0:
    print(Interesting_Function())
    reamined_test_cases -= 1 
