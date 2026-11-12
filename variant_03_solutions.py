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
            raise ZeroDivisionError("Похідна прямує до нуля")
        x_next=x_curr - f_val/df_val
        diff=abs(x_curr-x_next)
        log.append((i, x_curr, x_next, f_val, df_val, diff))
        if diff<eps:
            return x_next, i, log
        x_curr=x_next
    return x_curr, num_iter, log

def save_results_to_file(filename, root, i, eps, log):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Рівняння f(x)=arctg(1/x)-x^2=0\n")
        file.write("Метод: метод Ньютона\n")
        file.write(f"Точність (eps) - {eps}\n")
        file.write(f"Корінь: {root:.6f}\n")
        file.write(f"Кількість ітерацій: {i}\n\n")
        head= f"{'Ітер.':<6}|{'x_n':<11}|{'f(x_n)':<11}|{'f\'(x_n)':<11}|{'x_(n+1)':<11}|{'|x_(n+1)-x_n|':<16}\n"
        separ= "-"*len(head)
        file.write(head)
        file.write(f"{separ}\n")
        for iter, x_curr, x_next, f_val, df_val, diff in log:
            file.write(f"{iter:<6}|{x_curr:<11.6f}|{f_val:<11.6f}|{df_val:<11.6f}|{x_next:<11.6f}|{diff:<16.6f}\n")

def main():
    a, b = 0.1, 3
    x0=3
    eps = 0.00002
    log_filename = "results_variant_03.txt"
    root, i, log = solve_newton(f, df, x0, eps)
    print("Рівняння f(x)=arctg(1/x)-x^2=0")
    print("Метод: метод Ньютона")
    print(f"Точність (eps) - {eps}")
    print(f"Корінь: {root:.6f}")
    head= f"{'Ітер.':<6}|{'x_n':<11}|{'f(x_n)':<11}|{'f\'(x_n)':<11}|{'x_(n+1)':<11}|{'|x_(n+1)-x_n|':<16}"
    print(head)
    print(f"{"-"*len(head)}")
    for iter, x_curr, x_next, f_val, df_val, diff in log:
        print(f"{iter:<6}|{x_curr:<11.6f}|{f_val:<11.6f}|{df_val:<11.6f}|{x_next:<11.6f}|{diff:<16.6f}")
    save_results_to_file(log_filename, root, i, eps, log)
    print(f"Збережений звіт у файлі {log_filename}")
    print(log)

if __name__ == "__main__":
    main()