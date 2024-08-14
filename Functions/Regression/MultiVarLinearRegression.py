import copy
import numpy as np


def getYHat(w, X, b):
    tar = np.matmul(w, X.T) + b
    return tar


def getW(ww, X, Y, yhat, alpha):
    w = copy.copy(ww)
    S = [0 for _ in range(len(Y))]
    C = [0 for _ in range(X.shape[1])]
    for i in range(len(Y)):
        S[i] = yhat[i] - Y[i]
    for i in range(X.shape[1]):
        for j in range(len(Y)):
            C[i] += S[j] * X[j][i]
        C[i] /= len(Y)
        w[i] = ww[i] - alpha * C[i]
    return w


def lossFunc(yHat, Y):
    c = [0 for _ in range(len(Y))]
    for i in range(len(Y)):
        c[i] = (yHat[i] - Y[i]) ** 2
    s = sum(c)
    return s / len(Y)


def gradientDescent(X, Y, iter, alpha):
    if alpha is None:
        alpha = 0.001
    iterations = iter
    m = len(Y)
    w = [1 for _ in range(X.shape[1])]
    b = 1
    loss = []
    while iterations > 0:
        print(iter - iterations + 1)
        yhat = getYHat(w, X, b)
        w = getW(w, X, Y, yhat, alpha)
        derivB = np.sum(yhat - Y) / m
        b = b - alpha * derivB
        loss.append(lossFunc(yhat, Y))
        iterations -= 1
    print(w)
    return w, b, loss
