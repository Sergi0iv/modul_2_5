def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)

    return matrix


h = get_matrix(2, 4, 3)
b = get_matrix(3, 5, 123)
g = get_matrix(4, 6, 56)
for i in h, b, g:
    print(i)
