def Comparing_Strings():
    string1 = list(input())
    string2 = list(input())
    if len(string1) != len(string2):
        return "NO"
    not_same = 0   
    not_same_at = []

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            not_same_at.append(i)
            not_same += 1 

    if not_same == 2:
        string1[not_same_at[0]],string1[not_same_at[1]] = string1[not_same_at[1]],string1[not_same_at[0]]
        if string1 == string2:
            return "YES"
        
    return "NO"    

        
        
        

remained_test_cases = 1 
# remained_test_cases = int(input())
while remained_test_cases  > 0:
    print(Comparing_Strings())
    remained_test_cases -= 1 
    