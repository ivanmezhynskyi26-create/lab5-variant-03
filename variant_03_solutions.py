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
        log.append({"iter": i, "x_curr": x_curr, "x_next": x_next, "f_x": f_val, "df_x": df_val, "difference": diff})
        if diff<eps:
            return x_next, i, log
        x_curr=x_next
    return x_curr, num_iter, log

def save_results_to_file(filename, root, i, eps, log):
    with open(filename, "w", encoding="uf-8") as file:
        file.write("Рівняння f(x)=arctg(1/x)-x^2=0\n")
        file.write("Метод: метод Ньютона\n")
        file.write(f"Точність (eps) - {eps}\n")
        file.write(f"Корінь: {root}\n")
        file.write(f"Кількість ітерацій: {i}\n\n")
        head= f"{'Ітер.':<6}|{'x_n':<12}|{'f(x_n)':<12}|{'f\'(x_n)':<12}|{'x_(n+1)':<12}|{'|x_(n+1)-x_n|':<16}\n"
        separ= "-"*len(head)
        file.write(head)
        file.write(separ)
        for iter, x_curr, x_next, f_val, df_val, diff in log:
            file.write(f"{iter:<6}|{x_curr:<12.6f}|{f_val:<12.6f}|{df_val:<12.6f}|{x_next:<12.6f}|{diff:<16.6f}\n")

