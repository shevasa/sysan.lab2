# -*- coding: UTF8 -*-

from copy import deepcopy

from scipy import special
from openpyxl import Workbook

from system_grad_m import *
from coord_descent import *
from tabulate import tabulate as tb


class Calculate(object):

    def __init__(self, d):
        self.n = d['samples']
        self.deg = d['dimensions']
        self.filename_input = d['input_file']
        self.filename_output = d['output']
        self.dict = d['output']
        self.p = list(map(lambda x: x + 1, d['degrees']))  # на 1 більше, адже включає 0
        self.weights = d['weights']
        self.poly_type = d['poly_type']
        self.splitted_lambdas = d['lambda_multiblock']
        self.eps = 1E-6
        self.norm_error = 0.0
        self.error = 0.0

    def define_data(self):
        print('Define data starts')
        f = open(self.filename_input, 'r')
        # всі дані з file_input у плаваючому вікні
        self.datas = np.matrix([list(map(lambda x: float(x), f.readline().split())) for i in range(self.n)])
        # перелік сумарних ступенів [3,1,2] -> [3,4,6]
        self.degf = [sum(self.deg[:i + 1]) for i in range(len(self.deg))]

    def norm_data(self):
        print('Trans data starts')
        '''
        kk
        '''
        n, m = self.datas.shape
        vec = np.ndarray(shape=(n, m), dtype=float)
        for j in range(m):
            minv = np.min(self.datas[:, j])
            maxv = np.max(self.datas[:, j])
            for i in range(n):
                vec[i, j] = (self.datas[i, j] - minv) / (maxv - minv)
        self.data = np.matrix(vec)

    def _minimize_equation(self, A, b, type='cjg'):
        """
        Знаходить такий вектор x що |Ax-b|->min.
        :param A: Matrix A
        :param b: Vector b
        :return: Vector x
        """
        if type == 'lsq':
            return np.linalg.lstsq(A, b)[0]
        elif type == 'cjg':
            return calculate_coordinate_descent(A.T * A, A.T * b,
                                                self.eps)  # --------------------------оптимізація

    def define_norm_vectors(self):
        print('Define trans vectors starts')
        '''
        будує матриці X and Y
        :return:
        '''
        X1 = self.data[:, :self.degf[0]]
        X2 = self.data[:, self.degf[0]:self.degf[1]]
        X3 = self.data[:, self.degf[1]:self.degf[2]]
        # матриця векторів i.e.X = [[X11,X12],[X21],...]
        self.X = [X1, X2, X3]
        # кількість колонок в матриці Х
        self.mX = self.degf[2]
        # матриця, що складається з i.e. Y1,Y2
        self.Y = self.data[:, self.degf[2]:self.degf[3]]
        self.Y_ = self.datas[:, self.degf[2]:self.degf[3]]
        self.X_ = [self.datas[:, :self.degf[0]], self.datas[:, self.degf[0]:self.degf[1]],
                   self.datas[:, self.degf[1]:self.degf[2]]]

    def built_B(self):
        def B_average():
            '''
            вектор B це середнє із max і min in Y. B[i] =max Y[i,:]
            :return:
            '''
            b = np.tile((self.Y.max(axis=1) + self.Y.min(axis=1)) / 2, (1, self.deg[3]))
            return b

        def B_scaled():
            '''
            Vector B  = Y
            :return:
            '''
            return deepcopy(self.Y)

        if self.weights == u'Average':
            self.B = B_average()
        elif self.weights == u'Scaled':
            self.B = B_scaled()
        else:
            print(self.weights)
            exit('B not defined')

    def poly_func(self):
        '''
        Визначте функцію для поліномів
        :return: function
        '''
        if self.poly_type == 'chebyshev':
            self.poly_f = special.eval_sh_chebyt
        elif self.poly_type == 'legendre':
            self.poly_f = special.eval_sh_legendre
        elif self.poly_type == 'laguerre':
            self.poly_f = special.eval_laguerre
        elif self.poly_type == 'hermit':
            self.poly_f = special.eval_hermite

    def built_A(self):
        '''
        побудована матриця А на зсунутих многочленах Чебишева
        : param self.p: mas градусів для вектора X1, X2, X3, тобто
        : param self.X: це матриця, яка має вектори X1 - X3, наприклад
        : return: матриця A як ndarray
        '''

        def mA():
            '''
            :парам X: [X1, X2, X3]
            :парам p: [p1,p2,p3]
            :return: m = m1*p1+m2*p2+...
            '''
            m = 0
            for i in range(len(self.X)):
                m += self.X[i].shape[1] * (self.p[i] + 1)
            return m

        def coordinate(v, deg):
            '''
            : парам v: вектор
            : парам град: поліном ступеня чебишева
            : return: стовпець з чебишевським значенням координаційного вектора
            '''
            c = np.ndarray(shape=(self.n, 1), dtype=float)
            for i in range(self.n):
                c[i, 0] = self.poly_f(deg, v[i])
            return c

        def vector(vec, p):
            '''
            : парам vec: саме X складається з векторів X11, X12, ...
            : парам p: максимальний ступінь для чебишевого полінома
            : return: частина матриці A для вектора X1
            '''
            n, m = vec.shape
            a = np.ndarray(shape=(n, 0), dtype=float)
            for j in range(m):
                for i in range(p):
                    ch = coordinate(vec[:, j], i)
                    a = np.append(a, ch, 1)
            return a

        # k = mA()
        A = np.ndarray(shape=(self.n, 0), dtype=float)
        for i in range(len(self.X)):
            vec = vector(self.X[i], self.p[i])
            A = np.append(A, vec, 1)
        self.A = np.matrix(A)

    def lamb(self):
        lamb = np.ndarray(shape=(self.A.shape[1], 0), dtype=float)
        for i in range(self.deg[3]):
            if self.splitted_lambdas:
                boundary_1 = self.p[0] * self.deg[0]
                boundary_2 = self.p[1] * self.deg[1] + boundary_1
                lamb1 = self._minimize_equation(self.A[:, :boundary_1], self.B[:, i])
                lamb2 = self._minimize_equation(self.A[:, boundary_1:boundary_2], self.B[:, i])
                lamb3 = self._minimize_equation(self.A[:, boundary_2:], self.B[:, i])
                lamb = np.append(lamb, np.concatenate((lamb1, lamb2, lamb3)), axis=1)
            else:
                lamb = np.append(lamb, self._minimize_equation(self.A, self.B[:, i]), axis=1)
        self.Lamb = np.matrix(lamb)  # Lamb in full events

    def psi(self):
        def built_psi(lamb):
            '''
            повернути матрицю xi1 для b1 як матрицю
            :парам A:
            :парам lamb:
            :парам p:
            :return: матриця psi, для кожного Y
            '''
            psi = np.ndarray(shape=(self.n, self.mX), dtype=float)
            q = 0  # ітератор в ламб і А
            l = 0  # ітератор у стовпцях psi
            for k in range(len(self.X)):  # вибір Х1 або Х2 або Х3
                for s in range(self.X[k].shape[1]):  # вибір X11 або X12 або X13
                    for i in range(self.X[k].shape[0]):
                        psi[i, l] = self.A[i, q:q + self.p[k]] * lamb[q:q + self.p[k], 0]
                    q += self.p[k]
                    l += 1
            return np.matrix(psi)

        self.Psi = []  # як список, тому що  psi[i] це матриця(а не вектор)
        for i in range(self.deg[3]):
            self.Psi.append(built_psi(self.Lamb[:, i]))

    def built_a(self):
        self.a = np.ndarray(shape=(self.mX, 0), dtype=float)
        for i in range(self.deg[3]):
            a1 = self._minimize_equation(self.Psi[i][:, :self.degf[0]], self.Y[:, i])
            a2 = self._minimize_equation(self.Psi[i][:, self.degf[0]:self.degf[1]], self.Y[:, i])
            a3 = self._minimize_equation(self.Psi[i][:, self.degf[1]:], self.Y[:, i])

            self.a = np.append(self.a, np.vstack((a1, a2, a3)), axis=1)

    def built_F1i(self, psi, a):
        '''
        не використовувати; він використовується в наступній функції
        : парам psi: матриця psi (лише одна
        : парам a: вектор із фігурою = (6,1)
        : парам degf: = [3,4,6] // фібоначі град
        : return: матриця (трьох) компонентів з F1 F2 та F3
        '''
        m = len(self.X)  # m  = 3
        F1i = np.ndarray(shape=(self.n, m), dtype=float)
        k = 0  # точка початку стовпця до множення
        for j in range(m):  # 0 - 2
            for i in range(self.n):  # 0 - 49
                F1i[i, j] = psi[i, k:self.degf[j]] * a[k:self.degf[j], 0]
            k = self.degf[j]
        return np.matrix(F1i)

    def built_Fi(self):
        self.Fi = []
        for i in range(self.deg[3]):
            self.Fi.append(self.built_F1i(self.Psi[i], self.a[:, i]))

    def built_c(self):
        self.c = np.ndarray(shape=(len(self.X), 0), dtype=float)
        for i in range(self.deg[3]):
            self.c = np.append(self.c,
                               calculate_coordinate_descent(self.Fi[i].T * self.Fi[i], self.Fi[i].T * self.Y[:, i],
                                                            self.eps), \
                               axis=1)  # ---------------------------------------оптимізація

    def built_F(self):
        F = np.ndarray(self.Y.shape, dtype=float)
        for j in range(F.shape[1]):  # 2
            for i in range(F.shape[0]):  # 50
                F[i, j] = self.Fi[j][i, :] * self.c[:, j]
        self.F = np.matrix(F)
        self.norm_error = []
        for i in range(self.Y.shape[1]):
            self.norm_error.append(np.linalg.norm(self.Y[:, i] - self.F[:, i], np.inf))

    def built_F_(self):
        minY = self.Y_.min(axis=0)
        maxY = self.Y_.max(axis=0)
        self.F_ = np.multiply(self.F, maxY - minY) + minY
        self.error = []
        for i in range(self.Y_.shape[1]):
            self.error.append(np.linalg.norm(self.Y_[:, i] - self.F_[:, i], np.inf))

    def save_to_file(self):
        print('Save to file starts')
        wb = Workbook()
        # отримати активний worksheet
        ws = wb.active

        l = [None]

        ws.append(['Input data: X'])
        for i in range(self.n):
            ws.append(l + self.datas[i, :self.degf[3]].tolist()[0])
        ws.append([])

        ws.append(['Input data: Y'])
        for i in range(self.n):
            ws.append(l + self.datas[i, self.degf[2]:self.degf[3]].tolist()[0])
        ws.append([])

        ws.append(['X transformed:'])
        for i in range(self.n):
            ws.append(l + self.data[i, :self.degf[2]].tolist()[0])
        ws.append([])

        ws.append(['Y transformed:'])
        for i in range(self.n):
            ws.append(l + self.data[i, self.degf[2]:self.degf[3]].tolist()[0])
        ws.append([])

        ws.append(['matrix B:'])
        for i in range(self.n):
            ws.append(l + self.B[i].tolist()[0])
        ws.append([])

        ws.append(['matrix A:'])
        for i in range(self.A.shape[0]):
            ws.append(l + self.A[i].tolist()[0])
        ws.append([])

        ws.append(['matrix Lambda:'])
        for i in range(self.Lamb.shape[0]):
            ws.append(l + self.Lamb[i].tolist()[0])
        ws.append([])

        for j in range(len(self.Psi)):
            s = 'matrix Psi%i:' % (j + 1)
            ws.append([s])
            for i in range(self.n):
                ws.append(l + self.Psi[j][i].tolist()[0])
            ws.append([])

        ws.append(['matrix a:'])
        for i in range(self.mX):
            ws.append(l + self.a[i].tolist()[0])
        ws.append([])

        for j in range(len(self.Fi)):
            s = 'matrix F%i:' % (j + 1)
            ws.append([s])
            for i in range(self.Fi[j].shape[0]):
                ws.append(l + self.Fi[j][i].tolist()[0])
            ws.append([])

        ws.append(['matrix c:'])
        for i in range(len(self.X)):
            ws.append(l + self.c[i].tolist()[0])
        ws.append([])

        ws.append(['Y rebuilt transformed :'])
        for i in range(self.n):
            ws.append(l + self.F[i].tolist()[0])
        ws.append([])

        ws.append(['Y rebuilt :'])
        for i in range(self.n):
            ws.append(l + self.F_[i].tolist()[0])
        ws.append([])

        ws.append(['Error transformed (Y - F)'])
        ws.append(l + self.norm_error)

        ws.append(['Error (Y_ - F_))'])
        ws.append(l + self.error)

        wb.save(self.filename_output)

    def show(self):
        print('Solver show starts')
        text = []

        text.append('Input data: X')
        text.append(tb(np.array(self.datas[:, :self.degf[2]])))

        text.append('\nInput data: Y')
        text.append(tb(np.array(self.datas[:, self.degf[2]:self.degf[3]])))

        text.append('\nX transformed:')
        text.append(tb(np.array(self.data[:, :self.degf[2]])))

        text.append('\nY transformed:')
        text.append(tb(np.array(self.data[:, self.degf[2]:self.degf[3]])))

        text.append('\nmatrix B:')
        text.append(tb(np.array(self.B)))

        text.append('\nmatrix A:')
        text.append(tb(np.array(self.A)))

        text.append('\nmatrix Lambda:')
        text.append(tb(np.array(self.Lamb)))

        for j in range(len(self.Psi)):
            s = '\nmatrix Psi%i:' % (j + 1)
            text.append(s)
            text.append(tb(np.array(self.Psi[j])))

        text.append('\nmatrix a:')
        text.append(tb(self.a.tolist()))

        for j in range(len(self.Fi)):
            s = '\nmatrix F%i:' % (j + 1)
            text.append(s)
            text.append(tb(np.array(self.Fi[j])))

        text.append('\nmatrix c:')
        text.append(tb(np.array(self.c)))

        text.append('\nY rebuilt transformed :')
        text.append(tb(np.array(self.F)))

        text.append('\nY rebuilt :')
        text.append(tb(self.F_.tolist()))

        text.append('\nError transformed (Y - F)')
        text.append(tb([self.norm_error]))

        text.append('\nError (Y_ - F_))')
        text.append(tb([self.error]))

        return '\n'.join(text)

    def prepare(self):
        print('Solver prepare starts')
        self.define_data()
        self.norm_data()
        self.define_norm_vectors()
        self.built_B()
        self.poly_func()
        self.built_A()
        self.lamb()
        self.psi()
        self.built_a()
        self.built_Fi()
        self.built_c()
        self.built_F()
        self.built_F_()
        self.save_to_file()
