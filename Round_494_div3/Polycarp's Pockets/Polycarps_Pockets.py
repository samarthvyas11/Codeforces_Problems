from collections import Counter
def question1():

    number_of_coin = int(input())
    coin_value = list(map(int,input().split()))
    total_coin = Counter(coin_value)
    min_pockets = 0

    for i in total_coin.keys():
        min_pockets = max(total_coin[i],min_pockets)

    return min_pockets    
    

# remained_test_cases = int(input())
remained_test_cases = 1 
while remained_test_cases > 0:
    print(question1())
    remained_test_cases -= 1 