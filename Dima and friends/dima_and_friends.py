def Dima_and_Friends():
    total_friends = int(input())
    friend_showing_finger = list(map(int,input().split()))
    moves = sum(friend_showing_finger)
    total_people = total_friends + 1 
    count_cases = 0 # where she not have to work
    
    if (moves + 1) % total_people != 1:
        count_cases += 1 
    if (moves + 2) % total_people != 1:
        count_cases += 1 
    if (moves + 3) % total_people != 1:
        count_cases += 1 
    if (moves + 4) % total_people != 1:
        count_cases += 1
    if (moves + 5) % total_people != 1:
        count_cases += 1
        
    return count_cases
    
remained_test_cases = 1 
# remained_test_cases = int(input())
while remained_test_cases > 0:
    print(Dima_and_Friends())
    remained_test_cases -= 1 