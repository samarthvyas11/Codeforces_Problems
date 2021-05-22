def question2():
    
    encrupted_len = int(input())
    encrupted_msg = input()
    divisors = []

    if encrupted_len == 1:
        return encrupted_msg
    i = encrupted_len

    while i > 1:
        if encrupted_len % i == 0:
            divisors.append(i)
        i -= 1    
    # print(divisors)        
    while len(divisors) > 0:
        reverse_upto = divisors.pop()
        encrupted_msg = encrupted_msg[reverse_upto-1::-1] + encrupted_msg[reverse_upto:]
    # print(encrupted_msg)  
    return encrupted_msg    
    
        
        
# remained_test_cases = int(input())
remained_test_cases = 1 
while remained_test_cases > 0:
    print(question2())
    remained_test_cases -= 1 