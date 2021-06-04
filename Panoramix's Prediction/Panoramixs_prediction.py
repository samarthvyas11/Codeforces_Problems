
prime_numbers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]


def Panoramixs_Prediction():
    prime,next_prime = map(int,input().split())
    
    for num in range(len(prime_numbers)):
        if prime_numbers[num] > prime:
            if next_prime == prime_numbers[num]:
                return True
            return False    
    

remained_test_cases = 1 
# remained_test_cases = int(input())
while remained_test_cases > 0:
    if (Panoramixs_Prediction()):
        print("YES")
    else:
        print("NO")
    remained_test_cases -= 1 