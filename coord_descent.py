import numpy as np


def calculate_coordinate_descent(A, b, eps):
    '''
    Coordinate descent method that solve equation Ax = b with given accuracy
    :param A:matrix A
    :param b:vector b
    :param eps: accuracy
    :return: solution x
    '''
    x0 = np.vectorize(len(A.T))
    print(f'{len(A.T)}')
    n = len(A.T)  # числовой столбец
    xi1 = xi = np.zeros(shape=(n, 1), dtype=float)
    vi = ri = b  # початковий стан
    i = 0  # цикл для числової ітерації
    while True:
        try:
            i += 1
            ai = float(vi.T * ri) / float(vi.T * A * vi)  # альфа і
            for j in range(0, len(xi)):
                xi1[j] = xi[j] + ai * vi[j]
            # xi1 = xi+ai*vi # x i+1
            ri1 = ri - ai * A * vi  # r i+1
            betai = -float(vi.T * A * ri1) / float(vi.T * A * vi)  # бета і
            vi1 = ri1 + betai * vi
            if (np.linalg.norm(A * xi1 - b) < eps) or i > 10 * n:
                break
            else:
                xi, vi, ri = xi1, vi1, ri1
        except Exception:
            print("проблеми з мінімізацією")
    return np.matrix(xi1)
