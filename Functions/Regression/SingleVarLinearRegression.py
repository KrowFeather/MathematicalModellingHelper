import numpy as np
from sklearn.linear_model import LinearRegression


def singleVarLinearRegressionOLS(x, y):
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    n = len(x)
    sum_xx = 0
    sum_xy = 0
    for i in range(n):
        sum_xx += x[i] ** 2
        sum_xy += x[i] * y[i]
    w = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x ** 2)
    b = np.mean(y) - np.mean(x) * w
    print(w, b)
    return w, b


def singleVarLinearRegressionSKL(X, Y):
    X = X[:, np.newaxis]
    print(X)
    model = LinearRegression()
    model.fit(X, Y)
    return model.coef_, model.intercept_


def lossFunction(X, y, w, b):
    loss = w * X + b - y
    cost = np.sum(loss ** 2) / (2 * len(X))
    return cost


def gradientDescent(X, y, iter, alpha):
    w = 0.1
    b = 1
    eta = alpha
    loss_history = []
    for i in range(iter):
        loss_history.append(lossFunction(X, y, w, b))
        loss = w * X + b - y
        derivative_w = X.T.dot(loss) / len(X)
        derivative_b = sum(loss) * 1 / len(X)
        w = w - eta * derivative_w
        b = b - eta * derivative_b
    return w, b, loss_history
