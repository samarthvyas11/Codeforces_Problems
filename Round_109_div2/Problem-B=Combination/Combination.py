def question2():
    total_card = int(input())
    sort_accord_top = []
    sort_accord_down = []
    
    for  card in range(total_card):
        num_top,num_down = map(int,input().split())
        sort_accord_top.append([num_top,num_down])
        sort_accord_down.append([num_top,num_down])
        
    sort_accord_top.sort(key = lambda x:x[0])
    sort_accord_down.sort(key = lambda x:x[1])
    
    card_should_add = 1
    max_score = 0
    
    while len(sort_accord_down) > 0 and card_should_add > 0:
        if card_should_add == 1:
            card1 = sort_accord_down.pop()
            if card1[1] == 0:
                card11 = sort_accord_top.pop()
                max_score += card11[0]
                card_should_add += card11[1]
                break
            else:
                card_should_add += card1[1]
                max_score += card1[0]
                sort_accord_top.remove(card1)
        else:
            card1 = sort_accord_top.pop()
            max_score += card1[0]
            card_should_add += card1[1]
            sort_accord_down.remove(card1)
                
        card_should_add -= 1  
    return max_score    
        
        
        
        
    
# remained_test_cases = int(input())
remained_test_cases = 1 
while remained_test_cases > 0 :
    print(question2())
    remained_test_cases -= 1 