# A * B  ----> col_A == row_B
# [[col], []] ---> [[2, 3], [4, 4]]

def multiply(A, B):
    row_A = len(A)
    col_A = len(A[0])

    row_B = len(B)
    col_B = len(B[0])

    if col_A != row_B:
        raise "satr va sotun barabar"

    res = [[0 for col in range(col_B)] for row in range(row_A)]

    for row in range(row_A):
        for col in range(col_B):
            for k in range(col_A):
                res[row][col] += (A[row][k] * B[k][col])

    return res


D = [[0]*2]*2

D[0][0] = 1
print(D)

# A = [[1, 0], [0, 1]]
# B = [[1, 2, 4], [2, 4, 5], [1, 2, 3]]

# print(multiply(A, B))
