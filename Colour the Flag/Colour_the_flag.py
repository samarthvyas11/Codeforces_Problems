def Colour_the_Flag():
    N,M = map(int,input().split())
    grid = []
    count_dot = 0
    # for k in range(2):
    for i in range(N):
        row1 = input()
        count_dot += row1.count(".")
        grid.append(list(row1))
    if count_dot == N*M:
        grid[0][0] = "W"
        
    for k in range(2):
        for i in range(N):
            for j in range(M):
                if grid[i][j] != ".":
                    if grid[i][j] == "W":
                        next = "R"
                    else:
                        next = "W"

                # for left        
                    z = j-1
                    while z >= 0:
                        if grid[i][z] != ".":
                            if grid[i][z] == next:
                                break
                            else:
                               
                                return ["NO",[]]
                        else:
                            grid[i][z] = next
                            if next == "W":
                                next = "R"
                            else:
                                next = "W"
                        z -= 1
              # for right
                    if grid[i][j] == "W":
                            next = "R"
                    else:
                            next = "W"    
                    z = j + 1 

              
                    while z < M:
                        if grid[i][z] != ".":
                            if grid[i][z] == next:
                                break
                            else:
                                
                                return ["NO",[]]
                        else:
                            grid[i][z] = next
                            if next == "W":
                                next = "R"
                            else:
                                next = "W"
                        z += 1
             # for top 
                    if grid[i][j] == "W":
                            next = "R"
                    else:
                            next = "W"
                    z = i-1 
                    while z >= 0:
                        if grid[z][j] != ".":
                            if grid[z][j] == next:
                                break
                            else:
                                
                                return ["NO",[]]
                        else:
                            grid[z][j] = next
                            if next == "W":
                                next = "R"
                            else:
                                next = "W"
                        z -= 1

              # for bottom  
                    if grid[i][j] == "W":
                            next = "R"
                    else:
                            next = "W"
                    z = i+1 
                    while z < N:
                        if grid[z][j] != ".":
                            if grid[z][j] == next:
                                break
                            else:
                                
                                return ["NO",[]]
                        else:
                            grid[z][j] = next
                            if next == "W":
                                next = "R"
                            else:
                                next = "W"
                        z += 1
                    
    return ["YES",grid]        
                
                
remained_test_cases = 1 
remained_test_cases = int(input())
while remained_test_cases  > 0:
    ans = (Colour_the_Flag())
    if ans[0] == "NO":
        print("NO")
    else:
        print("YES")
        for i in range(len(ans[1])):
            row = ""
            for j in range(len(ans[1][0])):
                row += ans[1][i][j]
            print(row)    
            
    
    remained_test_cases -= 1 
    