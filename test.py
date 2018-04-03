
matrix = [
[1,2,3],
[3,4,5],
[5,6,7],
[7,8,9]
]
def flip_matrix_old_fashio(matrix):
    m = len(matrix)
    n = len(matrix[0])
    
    result = []
    for i in range(n):
        current_row = []
        for j in range(m):
            current_row.append(matrix[j][i])
        result.append(current_row)
    return result

print(flip_matrix_old_fashio(matrix))

