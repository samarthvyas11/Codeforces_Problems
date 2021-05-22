def question1():
    
    total_question,skill_limit = map(int,input().split())
    diff_quest = list(map(int,input().split())) #difficulty as per questions
    successfully_done = 0
    is_breaked = False
    
    
    for ques in range(total_question):
        if diff_quest[ques] > skill_limit:
            is_breaked = True
            break 
        else:
            successfully_done += 1
    ques = total_question - 1        
    if is_breaked:
        while diff_quest[ques] <= skill_limit:
            successfully_done += 1 
            ques -= 1 
    return successfully_done
    
        
        
# remained_test_cases = int(input())
remained_test_cases = 1 
while remained_test_cases > 0:
    print(question1())
    remained_test_cases -= 1 