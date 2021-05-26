def question1():

    total_coin = int(input())
    value_of_coin = list(map(int,input().split()))
    total_ruppee = sum(value_of_coin)
    value_of_coin.sort(reverse = True)
    ruppee_we_have = 0
    coin = 0

    while coin < total_coin:
        ruppee_we_have += value_of_coin[coin]
        if ruppee_we_have > total_ruppee / 2:
            return coin + 1 
        coin += 1  
  
    return coin        
        
        
        
# remained_test_cases = int(input())
remained_test_cases = 1 
while remained_test_cases > 0:
    print(question1())
    remained_test_cases -= 1 