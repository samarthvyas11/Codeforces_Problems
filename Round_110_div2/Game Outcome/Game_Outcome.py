def question1():

    matrix_size = int(input())
    matrix = []

    for i in range(matrix_size):
        row = list(map(int,input().split()))
        matrix.append(row)

    sum_rows = [0 for i in range(matrix_size)]
    sum_cols = [0 for i in range(matrix_size)]

    for row in range(matrix_size):
        for col in range(matrix_size):
            sum_rows[row] += matrix[row][col]
            sum_cols[col] += matrix[row][col]

    count_winning_squares = 0
    for row in range(matrix_size):
        for col in range(matrix_size):
            if sum_cols[col] > sum_rows[row]:
                count_winning_squares += 1 

    return count_winning_squares            
        
# remained_test_cases = int(input())
remained_test_cases = 1 
while remained_test_cases > 0:
    print(question1())
    remained_test_cases -= 1 