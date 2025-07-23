from sympy import symbols, sympify, lambdify

def runge_kutta(expr_str, t0, y0, tf, h):
    t, y = symbols('t y')
    f_expr = sympify(expr_str)
    f = lambdify((t, y), f_expr, modules=["numpy"])
    ts = [t0]
    ys = [y0]
    n = int((tf - t0) / h)
    for _ in range(n):
        k1 = h * f(t0, y0)
        k2 = h * f(t0 + h/2, y0 + k1/2)
        k3 = h * f(t0 + h/2, y0 + k2/2)
        k4 = h * f(t0 + h, y0 + k3)
        y0 = y0 + (k1 + 2*k2 + 2*k3 + k4) / 6
        t0 = t0 + h
        ts.append(t0)
        ys.append(y0)
    return ts, ys

def newton_raphson(expr_str, deriv_str, x0, tol):
    x = symbols('x')
    f = lambdify(x, sympify(expr_str), modules=["numpy"])
    df = lambdify(x, sympify(deriv_str), modules=["numpy"])
    x1 = x0 - f(x0)/df(x0)
    while abs(x1 - x0) > tol:
        x0 = x1
        x1 = x0 - f(x0)/df(x0)
    return x1