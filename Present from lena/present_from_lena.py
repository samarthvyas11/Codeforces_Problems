def Present_from_Lena():
    N = int(input())


    #UPPER HALF
    for i in range(N+1):
        for z in range(i,N):
            print(" ",end=" ")
        for j in range(i):
            print(j,end=" ")
        j = i
        while j >= 0:
            if j == 0:
                print(j)
            else:    
                print(j,end=" ")
            j -= 1



    #LOWER HALF
    for i in range(N):
        for j in range(i+1):
            print(" ",end = " ")
        if i == N-1:
            print(0)
        else:    
            for j in range(N-i):
                print(j,end=" ")
            j -= 1     
            while j >= 0:
                if j == 0:
                    print(j)
                else:    
                    print(j,end= " ")
                j -= 1 
            
            
            
    
    
    
remained_test_cases = 1 
# remained_test_cases = int(input())
while remained_test_cases > 0:
    (Present_from_Lena())
    remained_test_cases -= 1 