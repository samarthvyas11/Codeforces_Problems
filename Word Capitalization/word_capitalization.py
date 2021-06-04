def Word():
    word = list(input())
    if ord(word[0]) >= 97 :
        word[0] = chr(ord(word[0])-32)
    output = ""
    
    for w in word:
        output += w 
    return output    
    
    
remained_test_cases = 1 
# remained_test_cases = int(input())
while remained_test_cases > 0:
    print(Word())
    remained_test_cases -= 1 