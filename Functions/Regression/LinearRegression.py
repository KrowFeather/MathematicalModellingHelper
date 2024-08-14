import numpy as np


def singleVarLinearRegression(mat):
    print(mat)
    S = np.sum(mat, axis=0)
    sum_x = S[1]
    sum_y = S[2]
    n = mat.shape[1]
    sum_xx = 0
    sum_xy = 0
    for i in range(mat.shape[0]):
        sum_xx += mat[i][1] ** 2
        sum_xy += mat[i][1] * mat[i][2]
    w = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x ** 2)
    mean = np.mean(mat, axis=0)
    b = mean[2] - mean[1] * w
    print(w, b)
    return w, b
