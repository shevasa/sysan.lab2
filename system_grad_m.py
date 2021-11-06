import numpy as np


def conjugate_gradient_method(A, b, eps):
    '''
   Метод спряженого градієнта, який вирішує рівняння Ax = b із заданою точністю
    : param A: матриця A
    : param b: вектор b
    : param eps: точність
    : return: рішення x
    '''
    n = len(A.T)  # number column
    print('Починається оптимізація:')
    print(f'{A}')
    # print(f'{A.T}')
    xi1 = xi = np.zeros(shape=(n, 1), dtype=float)
    vi = ri = b  # початковий стан
    i = 0  # цикл для ітерації чисел
    while True:
        try:
            i += 1
            ai = float(vi.T * ri) / float(vi.T * A * vi)  # альфа i
            print(f'ai = {ai}\nvi = {vi}')
            xi1 = xi + ai * vi  # x i+1
            ri1 = ri - ai * A * vi  # r i+1
            betai = -float(vi.T * A * ri1) / float(vi.T * A * vi)  # бета i
            vi1 = ri1 + betai * vi
            if (np.linalg.norm(ri1) < eps) or i > 10 * n:
                break
            else:
                xi, vi, ri = xi1, vi1, ri1
        except Exception:
            print("проблеми з мінімізацією")
    print(f'Оптимізація закінчена:\nResult: {xi1}')
    return np.matrix(xi1)
