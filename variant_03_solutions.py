"""
Лабораторна робота: Функції та декомпозиція задач
Варіант: 3
Студент: Межинський Іван
Група: EIP-30
"""

import math
def f(x):
    if x==0:
        raise ValueError("Функція не визначена при x = 0")
    return math.atan(1/x)-x**2

def df(x):
    return -1/(x**2+1) - 2*x

def solve_newton(func, deriv, x0, eps, num_iter=50):
    log=[]
    x_curr=x0
    for i in range(1, num_iter+1):
        f_val=func(x_curr)
        df_val=deriv(x_curr)
        if abs(df_val) < 1e-9:
            raise "Похідна прямує до нуля"
        x_next=x_curr - f_val/df_val
        diff=abs(x_curr-x_next)
        log.append({"iter": i, "x_curr": x_curr, "f_x": f_val, "df_x": df_val, "difference": diff})
        if diff<eps:
            return x_next, i, log
        x_curr=x_next
    return x_curr, num_iter, log

 