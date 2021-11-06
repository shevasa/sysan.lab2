import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QColor

from main_window import *
from method import *
from findf import *
from show import PolynomialBuilder


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = UiMainWindow()
        self.ui.setupUi(self)
        # self.ui.QColor(self)
        # super().__init__()
        # self.setupUI()

        self.refresh_data()

        # other initializations
        """self.dimensions = [self.ui.X1Dimension.value(), self.ui.X2Dimension.value(),
                           self.ui.X3Dimension.value(), self.ui.YDimension.value()]
        self.degrees = [self.ui.X1Exponent.value(), self.ui.X2Exponent.value(), self.ui.X3Exponent.value()]
        self.type = 'null'
        if self.ui.ChebushevCheck.isChecked():
            self.type = 'chebyshev'
        elif self.ui.LegendreCheck.isChecked():
            self.type = 'legendre'
        elif self.ui.LaguerreCheck.isChecked():
            self.type = 'laguerre'
        elif self.ui.HermitCheck.isChecked():
            self.type = 'hermit'
        self.input_path = ''
        self.output_path = ''
        """
        self.ui.ExecuteButton.clicked.connect(self.execute_button_clicked)
        self.ui.GraphicButton.clicked.connect(self.graphic_button_clicked)
        self.ui.toolButton.clicked.connect(self.input_button_clicked)
        self.ui.toolButton_2.clicked.connect(self.output_button_clicked)
        self.ui.pushButton.clicked.connect(self.calc_clicked)

    def refresh_data(self):
        self.dimensions = [self.ui.X1Dimension.value(), self.ui.X2Dimension.value(),
                           self.ui.X3Dimension.value(), self.ui.YDimension.value()]
        self.degrees = [self.ui.X1Exponent.value(
        ), self.ui.X2Exponent.value(), self.ui.X3Exponent.value()]
        self.type = 'null'
        if self.ui.ChebyshevCheck.isChecked():
            self.type = 'chebyshev'
        elif self.ui.LegendreCheck.isChecked():
            self.type = 'legendre'
        elif self.ui.LaguerreCheck.isChecked():
            self.type = 'laguerre'
        elif self.ui.HermitCheck.isChecked():
            self.type = 'hermit'
        self.samples_num = self.ui.SampleSize.value()
        self.input_path = self.ui.InputFile.text()
        self.output_path = self.ui.OutputFile.text()
        self.lambda_multiblock = self.ui.LambdaCheck.isChecked()
        self.weight_method = self.ui.FunctionWeight.currentText()

    def calc_clicked(self):
        self.refresh_data()
        try:
            self.ui.pushButton.setEnabled(False)
            solver = Calculate(self.__get_params())
            solver.define_data()
            solver.norm_data()
            solver.define_norm_vectors()
            solver.built_B()
            solver.poly_func()
            d = self.degree(solver, 5, 5, 5)
            f1 = open('degree.txt', 'w')
            miner = d[0]
            for i in d:
                f1.write(str(i[0]) + ' : ' + str(i[1]))
                f1.write('\n')
                if i[1] < miner[1]:
                    miner = i
            QMessageBox.warning(self, 'Оптимальные степени', str(miner[0]))
            f1.close()
        except Exception as e:
            QMessageBox.warning(self, 'Error!' + str(e))
        self.ui.pushButton.setEnabled(True)
        return

    def graphic_button_clicked(self):
        if self.solution:
            try:
                self.solution.plot_graphs()
            except Exception as e:
                QMessageBox.warning(
                    self, 'Error!', 'Error happened during plotting: ' + str(e))
        return

    def input_button_clicked(self):
        input_file = Application().file
        self.ui.InputFile.setText(input_file)

    def execute_button_clicked(self):
        self.refresh_data()
        self.ui.ExecuteButton.setEnabled(False)
        try:
            print('Execute button pushed')
            solver = Calculate(self.__get_params())

            solver.prepare()
            solver.show()
            self.solution = PolynomialBuilder(solver)
            print('Init Polynomial builder finished')
            f = open(self.output_path, 'w')
            f.write(
                f'Main:\nSolver.show():\n{solver.show()}\n\nSolution.get_results():{self.solution.get_results()}')
            f.close()
            # self.output_path.setText(solver.show() + '\n\n' + self.solution.get_results())
        except Exception as e:
            QMessageBox.warning(self, 'Error! ' + str(e))
        self.ui.ExecuteButton.setEnabled(True)
        return

    def degree(self, a, p1, p2, p3):
        d = list()
        # d = dict()
        for i in range(1, p1):
            for j in range(1, p2):
                for k in range(1, p3):
                    a.p = [i + 1, j + 1, k + 1]
                    a.built_A()
                    a.lamb()
                    a.psi()
                    a.built_a()
                    a.built_Fi()
                    a.built_c()
                    a.built_F()
                    a.built_F_()
                    # d[str(i)+' '+str(j)+' '+str(k)] = [np.linalg.norm(a.F - a.Y), np.std(a.F_ - a.Y_, axis=0),\
                    #                   np.linalg.norm(a.F_ - a.Y_)]
                    d.append((str(i) + ' ' + str(j) + ' ' +
                              str(k), np.linalg.norm(a.norm_error)))
        return d

    def output_button_clicked(self):
        output = Application().file
        self.ui.OutputFile.setText(output)

    def mbox(self, body, title='Processing...'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()

    def __get_params(self):
        return dict(poly_type=self.type, degrees=self.degrees, dimensions=self.dimensions,
                    samples=self.samples_num, input_file=self.input_path, output=self.output_path,
                    weights=self.weight_method, lambda_multiblock=self.lambda_multiblock)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # app.setApplicationName('System analysis 2')
    myapp = MyWindow()
    myapp.show()
    sys.exit(app.exec_())
