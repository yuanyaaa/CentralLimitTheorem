# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CentralLimitWeget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 781)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.continue_ = QtWidgets.QPushButton(self.centralwidget)
        self.continue_.setGeometry(QtCore.QRect(780, 570, 91, 51))
        self.continue_.setObjectName("continue_")
        self.chooseDistribution = QtWidgets.QComboBox(self.centralwidget)
        self.chooseDistribution.setGeometry(QtCore.QRect(70, 570, 111, 41))
        self.chooseDistribution.setObjectName("chooseDistribution")
        self.chooseDistribution.addItem("")
        self.chooseDistribution.addItem("")
        self.chooseDistribution.addItem("")
        self.chooseDistribution.addItem("")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(730, 650, 160, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 20, 901, 521))
        self.graphicsView.setObjectName("graphicsView")
        self.normalization = QtWidgets.QRadioButton(self.centralwidget)
        self.normalization.setGeometry(QtCore.QRect(70, 640, 101, 41))
        self.normalization.setObjectName("normalization")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 570, 191, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 580, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 650, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 650, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(640, 570, 111, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(640, 640, 111, 41))
        self.label_6.setObjectName("label_6")
        self.sliderMin = QtWidgets.QLabel(self.centralwidget)
        self.sliderMin.setGeometry(QtCore.QRect(730, 680, 67, 17))
        self.sliderMin.setObjectName("sliderMin")
        self.sliderMax = QtWidgets.QLabel(self.centralwidget)
        self.sliderMax.setGeometry(QtCore.QRect(870, 680, 67, 17))
        self.sliderMax.setObjectName("sliderMax")
        self.rangemin = QtWidgets.QLineEdit(self.centralwidget)
        self.rangemin.setGeometry(QtCore.QRect(400, 570, 51, 41))
        self.rangemin.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.rangemin.setObjectName("rangemin")
        self.rangemax = QtWidgets.QLineEdit(self.centralwidget)
        self.rangemax.setGeometry(QtCore.QRect(510, 570, 51, 41))
        self.rangemax.setObjectName("rangemax")
        self.step = QtWidgets.QLineEdit(self.centralwidget)
        self.step.setGeometry(QtCore.QRect(320, 640, 51, 41))
        self.step.setObjectName("step")
        self.pro = QtWidgets.QLineEdit(self.centralwidget)
        self.pro.setGeometry(QtCore.QRect(510, 640, 51, 41))
        self.pro.setObjectName("pro")
        self.n_value = QtWidgets.QLineEdit(self.centralwidget)
        self.n_value.setGeometry(QtCore.QRect(910, 640, 51, 41))
        self.n_value.setObjectName("n_value")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 967, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.continue_.setText(_translate("MainWindow", "Start"))
        self.chooseDistribution.setItemText(0, _translate("MainWindow", "Binomial"))
        self.chooseDistribution.setItemText(1, _translate("MainWindow", "Poisson"))
        self.chooseDistribution.setItemText(2, _translate("MainWindow", "Chi2"))
        self.chooseDistribution.setItemText(3, _translate("MainWindow", "T"))
        self.normalization.setText(_translate("MainWindow", "标准化"))
        self.label.setText(_translate("MainWindow", "The range of n:"))
        self.label_2.setText(_translate("MainWindow", "-"))
        self.label_3.setText(_translate("MainWindow", "Step:"))
        self.label_4.setText(_translate("MainWindow", "P:"))
        self.label_5.setText(_translate("MainWindow", "连续播放"))
        self.label_6.setText(_translate("MainWindow", "逐帧播放"))
        self.sliderMin.setText(_translate("MainWindow", "0"))
        self.sliderMax.setText(_translate("MainWindow", "0"))
        self.menu.setTitle(_translate("MainWindow", "中心极限定理"))
