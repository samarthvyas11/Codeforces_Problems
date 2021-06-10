def Friends_and_Candies():
    total_friends = int(input())
    candies_friend_have= list(map(int,input().split()))
    total_candies = sum(candies_friend_have)
    if total_candies % total_friends != 0:
        return -1 
    to_each_friend = total_candies // total_friends
   
    minimum_select = 0
    
    
    for i in range(total_friends):
        if candies_friend_have[i] > to_each_friend:
            minimum_select += 1 
    return minimum_select
        
remained_test_cases = 1 
remained_test_cases = int(input())
while remained_test_cases > 0:
    print(Friends_and_Candies())
    remained_test_cases -= 1 