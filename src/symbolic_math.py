import sympy as sp

def symbolic_differentiation(expr, var):
    return sp.diff(expr, var)

def solve_equation(expr, var):
    return sp.solve(expr, var)

def taylor_series(expr, var, order):
    return expr.series(var, 0, order)
