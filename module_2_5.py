def get_matrix(n, m, value):
    matrix = []
    if n == 0 or m == 0:
        return matrix
    else:
        for i in range(n):
            matrix.append([])
            for j in range(m):
                matrix[i].append(value)
        return matrix

win = get_matrix(1, 5, 5)
print(win)
