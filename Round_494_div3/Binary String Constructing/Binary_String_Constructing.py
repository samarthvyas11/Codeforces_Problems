# from collections import Counter
def question2():

    avail_0,avail_1,pair_not_equal = map(int,input().split())

    if avail_0 > avail_1:

        if pair_not_equal % 2 != 0:
            avail_0 = avail_0 - (pair_not_equal//2) - 1
            avail_1 = avail_1 - pair_not_equal//2
            binary_string = "01"*(pair_not_equal//2)+ "0" +"0"*avail_0 + "1"*avail_1
        else:
            
            avail_0 = avail_0 - (pair_not_equal//2)-1
            avail_1 = avail_1 - pair_not_equal//2
            binary_string = "0"*avail_0 + "01"*(pair_not_equal//2) + "1"*avail_1+"0"
            
      
        return binary_string
    else:
        if pair_not_equal % 2 != 0:
            avail_1 = avail_1 - (pair_not_equal//2) - 1
            avail_0 = avail_0 - pair_not_equal//2
            binary_string = "10"*(pair_not_equal//2)+ "1" +"1"*avail_1 + "0"*avail_0
        else:
            
            avail_1 = avail_1 - (pair_not_equal//2)-1
            avail_0 = avail_0 - pair_not_equal//2
            binary_string = "1"*avail_1 + "10"*(pair_not_equal//2) + "0"*avail_0+"1"
            
      
        return binary_string
        
 
  

# remained_test_cases = int(input())
remained_test_cases = 1 
while remained_test_cases > 0:
    print(question2())
    remained_test_cases -= 1 