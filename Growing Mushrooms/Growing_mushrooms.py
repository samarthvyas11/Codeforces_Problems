def Growing_Mushrooms():
    total_grower,slot1,slot2,loss_in_break = map(int,input().split())
    scorecard = []
    loss_in_break = loss_in_break / 100

    for i in range(total_grower):
        speed1,speed2 = map(int,input().split())
        result_height = max(speed1*slot1*(1-loss_in_break)+speed2*slot2 , speed2*slot1*(1-loss_in_break)+speed1*slot2)
        scorecard.append([i+1,result_height])
    scorecard.sort(key = lambda x:x[1],reverse = True)
    return scorecard

        
    
remained_test_cases = 1 
# remained_test_cases = int(input())
while remained_test_cases  > 0:
    scorecard = (Growing_Mushrooms())
    for i in range(len(scorecard)):
        print(scorecard[i][0],"{:.2f}".format(scorecard[i][1]))
    remained_test_cases -= 1 
    