def UltraFast_Mathematician():
    number1 = input()
    number2 = input()
    output = ""
    
    for i in range(len(number1)):
        if number1[i] == number2[i]:
            output += "0"
        else:
            output += "1"
    return output        
    
    

remained_test_cases = 1 
# remained_test_cases = int(input())
while remained_test_cases > 0:
    print(UltraFast_Mathematician())
    remained_test_cases -= 1 