def question3():
    string_len,remove_left = map(int,input().split())
    string = input()
    
    alpha_count = [0 for i in range(26)] #alphabet count 
    
    
    for character in string:
        alpha_count[ord(character)-97] += 1 
        
        
    remove_alpha_upto = [0 for i in range(26)] #no. of times an alphabet should remove(a=index(0),b=index(1)....z=index(26))
    
    for i in range(26):
        if remove_left >= alpha_count[i]:
            remove_alpha_upto[i] = alpha_count[i]
            remove_left -= alpha_count[i]
        else:
            remove_alpha_upto[i] = remove_left
            remove_left = 0 
        if remove_left == 0:
            break 
        
    done_string = ""
    
    for character in string:
        if remove_alpha_upto[ord(character)-97] <= 0:
            done_string += character
        else:
            remove_alpha_upto[ord(character)-97] -= 1 
            
    return done_string        
            
            
    
# remained_test_cases = int(input())
remained_test_cases = 1 
while remained_test_cases > 0:
    print(question3())
    remained_test_cases -= 1 