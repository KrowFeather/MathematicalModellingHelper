def normalization(mat):
    standard = [0 for i in range(mat.shape[1])]
    for i in range(mat.shape[0]):
        for j in range(1, mat.shape[1]):
            standard[j] += mat[i][j] ** 2
    for i in range(len(standard)):
        standard[i] = standard[i] ** 0.5
    for i in range(mat.shape[0]):
        for j in range(1, mat.shape[1]):
            mat[i][j] /= standard[j]
    print(mat)
