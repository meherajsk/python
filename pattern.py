def generate_pattern(N):
    matrix = [[0] * N for _ in range(N)]
    num = 1
    
    # Fill the matrix column by column
    for col in range(N):
        for row in range(N):
            if col == 0:
                matrix[row][col] = num
                num += row + 1
            else:
                matrix[row][col] = matrix[row][col-1] + col
    
    # Print the matrix
    for row in matrix:
        print(" ".join(map(str, row)))

# Input value
N = 4
generate_pattern(N)
