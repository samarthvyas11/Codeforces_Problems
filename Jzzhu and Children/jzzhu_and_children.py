import math
def Jzzhu_and_Children():
    total_childrens,chocolate_per_step = map(int,input().split())
    chocolate_need = list(map(int,input().split()))
    in_turns = []
    
    for choc in range(total_childrens):
        in_turns.append(math.ceil(chocolate_need[choc]/chocolate_per_step))
    max1 = max(in_turns)
    # print(in_turns)
    
    length = total_childrens - 1 
    while length >= 0:
        if in_turns[length] == max1:
            return length+1 
        length -= 1     
    
    
remained_test_cases = 1 
# remained_test_cases = int(input())
while remained_test_cases > 0:
    print(Jzzhu_and_Children())
    remained_test_cases -= 1 