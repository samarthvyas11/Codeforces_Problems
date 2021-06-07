def Drinks():
    total_drinks = int(input())
    percent_orange_in = list(map(int,input().split()))
    total_volume = 100 * total_drinks
    volume_of_orange = 0

    for drink in range(total_drinks):
        volume_of_orange += percent_orange_in[drink]

    percent_orange_in_final = (volume_of_orange/total_volume) * 100 
    return percent_orange_in_final
    
remained_test_cases = 1 
# remained_test_cases = int(input())
while remained_test_cases > 0:
    print(Drinks())
    remained_test_cases -= 1 