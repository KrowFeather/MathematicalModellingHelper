from scipy.optimize import linprog


def linearProgramming(c, A_ub, B_ub, A_eq, B_eq, bounds):
    print(c)
    print(A_ub)
    print(B_ub)
    print(A_eq)
    print(B_eq)
    for i in range(len(bounds)):
        bounds[i][0] = 0
    print(bounds)
    result = linprog(c=c, A_ub=A_ub, b_ub=B_ub, A_eq=A_eq, bounds=bounds, b_eq=B_eq)
    print(result)
    print(result.x)
    return result
