# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)

        MainWindow.setStyleSheet(
            "background-color:#EDB7F5; color: #000000; font: 17px verdana;font-weight:bold")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(640, 10, 500, 700))
        self.groupBox.setObjectName("groupBox")

        self.groupBox.setStyleSheet(
            "background-color:#FBFBFB;font-weight:bold")

        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(250, 200, 220, 241))
        self.groupBox_2.setObjectName("groupBox_2")

        self.groupBox_2.setStyleSheet(
            "background-color:#E788F5;background-color:#E788F5")

        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 40, 170, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ChebyshevCheck = QtWidgets.QRadioButton(self.layoutWidget)
        self.ChebyshevCheck.setObjectName("ChebyshevCheck")
        self.verticalLayout.addWidget(self.ChebyshevCheck)
        self.LegendreCheck = QtWidgets.QRadioButton(self.layoutWidget)
        self.LegendreCheck.setObjectName("LegendreCheck")
        self.verticalLayout.addWidget(self.LegendreCheck)
        self.LaguerreCheck = QtWidgets.QRadioButton(self.layoutWidget)
        self.LaguerreCheck.setObjectName("LaguerreCheck")
        self.verticalLayout.addWidget(self.LaguerreCheck)
        self.HermitCheck = QtWidgets.QRadioButton(self.layoutWidget)
        self.HermitCheck.setObjectName("HermitCheck")
        self.verticalLayout.addWidget(self.HermitCheck)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(58, 350, 120, 250))
        self.groupBox_3.setObjectName("groupBox_3")

        self.groupBox_3.setStyleSheet(
            "background-color:#E788F5")

        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 40, 85, 171))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")

        self.horizontalLayout_7.addWidget(self.label_7)
        self.X1Exponent = QtWidgets.QSpinBox(self.layoutWidget1)
        self.X1Exponent.setObjectName("X1Exponent")

        self.X1Exponent.setStyleSheet(
            "background-color:white;")

        self.horizontalLayout_7.addWidget(self.X1Exponent)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")

        self.horizontalLayout_6.addWidget(self.label_6)
        self.X2Exponent = QtWidgets.QSpinBox(self.layoutWidget1)
        self.X2Exponent.setObjectName("X2Exponent")

        self.X2Exponent.setStyleSheet(
            "background-color:white;")

        self.horizontalLayout_6.addWidget(self.X2Exponent)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")

        self.horizontalLayout_5.addWidget(self.label_5)
        self.X3Exponent = QtWidgets.QSpinBox(self.layoutWidget1)
        self.X3Exponent.setObjectName("X3Exponent")

        self.X3Exponent.setStyleSheet(
            "background-color:white;")

        self.horizontalLayout_5.addWidget(self.X3Exponent)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(50, 35, 130, 250))
        self.groupBox_4.setObjectName("groupBox_4")

        self.groupBox_4.setStyleSheet(
            "background-color:#E788F5")

        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 40, 86, 171))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setObjectName("label")

        self.horizontalLayout_4.addWidget(self.label)
        self.X1Dimension = QtWidgets.QSpinBox(self.layoutWidget2)
        self.X1Dimension.setObjectName("X1Dimension")

        self.X1Dimension.setStyleSheet("background-color:white;")

        self.horizontalLayout_4.addWidget(self.X1Dimension)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout_3.addWidget(self.label_2)
        self.X2Dimension = QtWidgets.QSpinBox(self.layoutWidget2)
        self.X2Dimension.setObjectName("X2Dimension")

        self.X2Dimension.setStyleSheet("background-color:white;")

        self.horizontalLayout_3.addWidget(self.X2Dimension)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setObjectName("label_3")

        self.horizontalLayout_2.addWidget(self.label_3)
        self.X3Dimension = QtWidgets.QSpinBox(self.layoutWidget2)
        self.X3Dimension.setObjectName("X3Dimension")

        self.X3Dimension.setStyleSheet("background-color:white;")

        self.horizontalLayout_2.addWidget(self.X3Dimension)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setObjectName("label_4")

        self.horizontalLayout.addWidget(self.label_4)
        self.YDimension = QtWidgets.QSpinBox(self.layoutWidget2)
        self.YDimension.setObjectName("YDimension")

        self.YDimension.setStyleSheet("background-color:white;")

        self.horizontalLayout.addWidget(self.YDimension)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(30, 20, 530, 250))
        self.groupBox_5.setObjectName("groupBox_5")

        self.groupBox_5.setStyleSheet(
            "background-color:#FBFBFB; font-weight:bold;")

        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_5)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 30, 255, 28))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_8.setObjectName("label_8")

        self.horizontalLayout_8.addWidget(self.label_8)
        self.SampleSize = QtWidgets.QSpinBox(self.layoutWidget3)
        self.SampleSize.setObjectName("SampleSize")

        self.horizontalLayout_8.addWidget(self.SampleSize)
        self.InputFile = QtWidgets.QLineEdit(self.groupBox_5)
        self.InputFile.setGeometry(QtCore.QRect(200, 115, 240, 25))
        self.InputFile.setObjectName("InputFile")
        self.toolButton = QtWidgets.QToolButton(self.groupBox_5)

        self.toolButton.setStyleSheet("background-color:#E788F5;")

        self.toolButton.setGeometry(QtCore.QRect(450, 115, 26, 24))
        self.toolButton.setObjectName("toolButton")
        self.OutputFile = QtWidgets.QLineEdit(self.groupBox_5)
        self.OutputFile.setGeometry(QtCore.QRect(210, 195, 225, 25))
        self.OutputFile.setObjectName("OutputFile")
        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox_5)
        self.toolButton_2.setGeometry(QtCore.QRect(450, 195, 26, 24))
        self.toolButton_2.setObjectName("toolButton_2")

        self.toolButton_2.setStyleSheet("background-color:#E788F5;")

        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setGeometry(QtCore.QRect(10, 120, 175, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setGeometry(QtCore.QRect(10, 200, 185, 17))
        self.label_11.setObjectName("label_11")

        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(30, 550, 540, 140))
        self.groupBox_6.setObjectName("groupBox_6")

        self.groupBox_6.setStyleSheet(
            "background-color:#FBFBFB;font-weight:bold")

        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_6)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 25, 480, 30))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)

        self.FunctionWeight = QtWidgets.QComboBox(self.layoutWidget4)
        self.FunctionWeight.setObjectName("FunctionWeight")
        self.FunctionWeight.addItem("Average")
        self.FunctionWeight.addItem("Scaled")
        self.horizontalLayout_9.addWidget(self.FunctionWeight)
        self.LambdaCheck = QtWidgets.QCheckBox(self.groupBox_6)
        self.LambdaCheck.setGeometry(QtCore.QRect(10, 70, 510, 30))
        self.LambdaCheck.setObjectName("LambdaCheck")

        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(30, 280, 540, 260))

        self.groupBox_7.setStyleSheet(
            "background-color:#FBFBFB;font-weight:bold")

        self.groupBox_7.setObjectName("groupBox_7")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton.setGeometry(QtCore.QRect(90, 190, 361, 40))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.setStyleSheet("background-color:#E788F5;")

        self.GraphicButton = QtWidgets.QPushButton(self.groupBox_7)
        self.GraphicButton.setGeometry(QtCore.QRect(90, 120, 361, 40))
        self.GraphicButton.setObjectName("GraphicButton")

        self.GraphicButton.setStyleSheet("background-color:#E788F5;")

        self.ExecuteButton = QtWidgets.QPushButton(self.groupBox_7)
        self.ExecuteButton.setGeometry(QtCore.QRect(90, 50, 361, 40))
        self.ExecuteButton.setObjectName("ExecuteButton")

        self.ExecuteButton.setStyleSheet("background-color:#E788F5;")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1070, 22))
        self.menubar.setObjectName("menubar")

        self.menubar.setStyleSheet("background-color:#90EE90;")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate(
            "MainWindow", "                              Поліном"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Тип"))
        self.ChebyshevCheck.setText(_translate("MainWindow", "Чебишева"))
        self.LegendreCheck.setText(_translate("MainWindow", "Лежандра"))
        self.LaguerreCheck.setText(_translate("MainWindow", "Лагера"))
        self.HermitCheck.setText(_translate("MainWindow", "Ерміта"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Ступені"))
        self.label_7.setText(_translate("MainWindow", "X1"))
        self.label_6.setText(_translate("MainWindow", "X2"))
        self.label_5.setText(_translate("MainWindow", "X3"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Розмірність"))
        self.label.setText(_translate("MainWindow", "X1"))
        self.label_2.setText(_translate("MainWindow", "X2"))
        self.label_3.setText(_translate("MainWindow", "X3"))
        self.label_4.setText(_translate("MainWindow", "Y"))
        self.groupBox_5.setTitle(_translate(
            "MainWindow", "                             Ініціалізація"))
        self.label_8.setText(_translate("MainWindow", "Розмір вибірки:"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.label_10.setText(_translate("MainWindow", "Вхідні данні (txt):"))
        self.label_11.setText(_translate("MainWindow", "Вихідні данні (txt):"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Additional"))
        self.label_9.setText(_translate(
            "MainWindow", "Weights of target functions:"))
        # self.FunctionWeight.setCurrentText(_translate("MainWindow", "Scaled"))
        # self.FunctionWeight.setItemText(0, _translate("MainWindow", "Average"))
        self.LambdaCheck.setText(_translate(
            "MainWindow", "Calculate group from 3 systems of equations?"))
        self.groupBox_7.setTitle(_translate(
            "MainWindow", "                                Виконання"))
        self.pushButton.setText(_translate(
            "MainWindow", "Знайти Оптимальний ступінь"))
        self.GraphicButton.setText(_translate("MainWindow", "Графік"))
        self.ExecuteButton.setText(_translate("MainWindow", "Виконати"))
