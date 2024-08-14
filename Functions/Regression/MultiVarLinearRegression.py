import numpy as np


def lossFunction(X, y, w, b):
    loss = w * X + b - y
    cost = np.sum(loss ** 2) / (2 * len(X))
    return cost


def gradientDescent(X, y):
    iter = 100
    w = 0.1
    b = 1
    eta = 0.000002
    loss_history = []
    for i in range(iter):
        print(i)
        loss_history.append(lossFunction(X, y, w, b))
        loss = w * X + b - y
        derivative_w = X.T.dot(loss) / len(X)
        derivative_b = sum(loss) * 1 / len(X)
        w = w - eta * derivative_w
        b = b - eta * derivative_b
    return w, b, loss_history
