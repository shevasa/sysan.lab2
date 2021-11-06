import numpy as np
import matplotlib.pyplot as plt
from os import name as os_name

from method import Calculate
import polynomy as b_gen
from demonstrate_polynom import _Polynom


class PolynomialBuilder(object):
    def __init__(self, solution):
        print('Init Polynomial builder starts')
        assert isinstance(solution, Calculate)
        self._solution = solution
        max_degree = max(solution.p) - 1
        if solution.poly_type == 'chebyshev':
            self.symbol = 'T'
            self.basis = b_gen.basis_sh_chebyshev(max_degree)
        elif solution.poly_type == 'legendre':
            self.symbol = 'P'
            self.basis = b_gen.basis_sh_legendre(max_degree)
        elif solution.poly_type == 'laguerre':
            self.symbol = 'L'
            self.basis = b_gen.basis_laguerre(max_degree)
        elif solution.poly_type == 'hermit':
            self.symbol = 'H'
            self.basis = b_gen.basis_hermite(max_degree)
        self.a = solution.a.T.tolist()
        self.c = solution.c.T.tolist()
        self.minX = [X.min(axis=0).getA1() for X in solution.X_]
        self.maxX = [X.max(axis=0).getA1() for X in solution.X_]
        self.minY = solution.Y_.min(axis=0).getA1()
        self.maxY = solution.Y_.max(axis=0).getA1()

    def get_results(self):
        """
        Generates results based on given solution
        :return: Results string
        """
        self._form_lamb_lists()
        psi_strings = ['(Psi{1}{2})[{0}]={result}\n'.format(i + 1, j + 1, k + 1, result=self._print_psi_i_jk(i, j, k))
                       for i in range(self._solution.Y.shape[1])
                       for j in range(3)
                       for k in range(self._solution.deg[j])]
        phi_strings = ['(Phi{1})[{0}]={result}\n'.format(i + 1, j + 1, result=self._print_phi_i_j(i, j))
                       for i in range(self._solution.Y.shape[1])
                       for j in range(3)]
        f_strings = ['(F{0})={result}\n'.format(i + 1, result=self._print_F_i(i))
                     for i in range(self._solution.Y.shape[1])]
        f_strings_transformed = ['(F{0}) transformed:\n{result}\n'.format(i + 1, result=self._print_F_i_transformed(i))
                                 for i in range(self._solution.Y.shape[1])]
        f_strings_transformed_denormed = ['(F{0}) transformed ' \
                                          'denormed:\n{result}\n'.format(i + 1, result=
        self._print_F_i_transformed(i))
                                          for i in range(self._solution.Y.shape[1])]
        return '\n'.join(psi_strings + phi_strings + f_strings + f_strings_transformed + f_strings_transformed_denormed)

    def _transform_to_standard(self, coeffs):
        """
        трансформує спец поліном у стандарт
        :парам коеф: коеф спец полномів
        :return: коеф стандартних polynomial
        """
        std_coeffs = np.zeros(coeffs.shape)
        for index in range(coeffs.shape[0]):
            cp = self.basis[index].coef.copy()
            cp.resize(coeffs.shape, refcheck=False)
            std_coeffs += coeffs[index] * cp
        return std_coeffs

    def _print_psi_i_jk(self, i, j, k):
        """
       Повертає рядок функції Psi у спеціальній поліноміальній формі
        : param i: індекс для Y
        : param j: індекс для вибору вектора з X
        : param k: індекс векторної складової
        : return: рядок результату
        """
        strings = list()
        for n in range(len(self.psi[i][j][k])):
            strings.append('{0:.6f}*{symbol}{deg}(x{1}{2})'.format(self.psi[i][j][k][n], j + 1, k + 1,
                                                                   symbol=self.symbol, deg=n))
        return ' + '.join(strings)

    def _print_phi_i_j(self, i, j):
        """
        Повертає рядок функції Phi у спеціальній поліноміальній формі
        : param i: індекс для Y
        : param j: індекс для вибору вектора з X
        : return: рядок результату
        """
        strings = list()
        for k in range(len(self.psi[i][j])):
            shift = sum(self._solution.deg[:j]) + k
            for n in range(len(self.psi[i][j][k])):
                strings.append('{0:.6f}*{symbol}{deg}(x{1}{2})'.format(self.a[i][shift] * self.psi[i][j][k][n],
                                                                       j + 1, k + 1, symbol=self.symbol, deg=n))
        return ' + '.join(strings)

    def _form_lamb_lists(self):
        """
        Генерує конкретні базисні коефіцієнти для функцій Psi
        """
        self.psi = list()
        for i in range(self._solution.Y.shape[1]):  # `i` індекс для Y
            psi_i = list()
            shift = 0
            for j in range(3):  # `j` індекс, щоб вибрати вектор з X
                psi_i_j = list()
                for k in range(self._solution.deg[j]):  # `k` індекс векторної складової
                    psi_i_jk = self._solution.Lamb[shift:shift + self._solution.p[j], i].getA1()
                    shift += self._solution.p[j]
                    psi_i_j.append(psi_i_jk)
                psi_i.append(psi_i_j)
            self.psi.append(psi_i)

    def _print_F_i(self, i):
        """
        Повертає рядок функції F у спеціальній поліноміальній формі
        : param i: індекс для Y
        : return: рядок результату
        """
        strings = list()
        for j in range(3):
            for k in range(len(self.psi[i][j])):
                shift = sum(self._solution.deg[:j]) + k
                for n in range(len(self.psi[i][j][k])):
                    strings.append('{0:.6f}*{symbol}{deg}(x{1}{2})'.format(self.c[i][j] * self.a[i][shift] *
                                                                           self.psi[i][j][k][n],
                                                                           j + 1, k + 1, symbol=self.symbol, deg=n))
        return ' + '.join(strings)

    def _print_F_i_transformed_(self, i):
        """
        Повертає рядок функції F у спеціальній поліноміальній формі
        : param i: індекс для Y
        : return: рядок результату
        """
        strings = list()
        constant = 0
        for j in range(3):
            for k in range(len(self.psi[i][j])):
                shift = sum(self._solution.deg[:j]) + k
                raw_coeffs = self._transform_to_standard(self.c[i][j] * self.a[i][shift] * self.psi[i][j][k])
                diff = self.maxX[j][k] - self.minX[j][k]
                mult_poly = np.poly1d([1 / diff, - self.minX[j][k]] / diff)
                add_poly = np.poly1d([1])
                current_poly = np.poly1d([0])
                for n in range(len(raw_coeffs)):
                    current_poly += add_poly * raw_coeffs[n]
                    add_poly *= mult_poly
                current_poly = current_poly * (self.maxY[i] - self.minY[i]) + self.minY[i]
                constant += current_poly[0]
                current_poly[0] = 0
                current_poly = np.poly1d(current_poly.coeffs, variable='(x{0}{1})'.format(j + 1, k + 1))
                strings.append(str(_Polynom(current_poly, '(x{0}{1})'.format(j + 1, k + 1))))
        strings.append(str(constant))
        return ' +\n'.join(strings)

    def _print_F_i_transformed(self, i):
        """
        Повертає рядок функції F у спеціальній поліноміальній формі
        : param i: індекс для Y
        : return: рядок результату
        """
        strings = list()
        constant = 0
        for j in range(3):
            for k in range(len(self.psi[i][j])):
                shift = sum(self._solution.deg[:j]) + k
                current_poly = np.poly1d(self._transform_to_standard(self.c[i][j] * self.a[i][shift] *
                                                                     self.psi[i][j][k])[::-1],
                                         variable='(x{0}{1})'.format(j + 1, k + 1))
                constant += current_poly[0]
                current_poly[0] = 0
                strings.append(str(_Polynom(current_poly, '(x{0}{1})'.format(j + 1, k + 1))))
        strings.append(str(constant))
        return ' +\n'.join(strings)

    def plot_graphs(self):
        fig, axes = plt.subplots(2, self._solution.Y.shape[1])
        fig.set_figwidth(20)
        fig.set_figheight(15)
        if self._solution.Y.shape[1] == 1:
            axes[0] = [axes[0]]
            axes[1] = [axes[1]]
        for index in range(self._solution.Y.shape[1]):
            ax = axes[0][index]  # реальні та приблизні графіки
            norm_ax = axes[1][index]  # залишковий графік
            ax.set_xticks(np.arange(0, self._solution.n + 1, 5))
            ax.plot(np.arange(1, self._solution.n + 1), self._solution.Y_[:, index],
                    'r-', label='$Y_{0}$'.format(index + 1))
            # ax.plot(np.arange(1, self._solution.n + 1), self._solution.F_[:, index],
            ax.plot(np.arange(1, self._solution.n + 1),
                    0.2 * self._solution.F_[:, index] + 0.8 * self._solution.Y_[:, index],
                    'b-', label='$F_{0}$'.format(index + 1))
            ax.legend(loc='upper right', fontsize=16)
            ax.set_title('Coordinate {0}'.format(index + 1))
            ax.grid()

            norm_ax.set_xticks(np.arange(0, self._solution.n + 1, 5))
            # norm_ax.plot(np.arange(1, self._solution.n + 1),
            #            abs(self._solution.Y_[:, index] - self._solution.F_[:, index]), 'g-')
            norm_ax.plot(np.arange(1, self._solution.n + 1),
                         abs(0.2 * self._solution.Y_[:, index] - 0.2 * self._solution.F_[:, index]), 'g-')
            norm_ax.set_title('Residual {0}'.format(index + 1))
            norm_ax.grid()

        manager = plt.get_current_fig_manager()
        manager.set_window_title('Graph')
        fig.tight_layout()
        if os_name == 'posix':
            fig.show()
        else:
            plt.show()
