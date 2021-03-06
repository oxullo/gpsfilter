# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sun Feb 10 00:44:15 2013
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(887, 612)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.graph = Graph(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph.sizePolicy().hasHeightForWidth())
        self.graph.setSizePolicy(sizePolicy)
        self.graph.setMinimumSize(QtCore.QSize(400, 0))
        self.graph.setObjectName(_fromUtf8("graph"))
        self.verticalLayout_2.addWidget(self.graph)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lbFileName = QtGui.QLabel(self.groupBox)
        self.lbFileName.setObjectName(_fromUtf8("lbFileName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lbFileName)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lbAscent = QtGui.QLabel(self.groupBox)
        self.lbAscent.setObjectName(_fromUtf8("lbAscent"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lbAscent)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.lbPoints = QtGui.QLabel(self.groupBox)
        self.lbPoints.setObjectName(_fromUtf8("lbPoints"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lbPoints)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lbDescent = QtGui.QLabel(self.groupBox)
        self.lbDescent.setObjectName(_fromUtf8("lbDescent"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lbDescent)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.rbMedian = QtGui.QRadioButton(self.groupBox_2)
        self.rbMedian.setChecked(True)
        self.rbMedian.setObjectName(_fromUtf8("rbMedian"))
        self.verticalLayout_4.addWidget(self.rbMedian)
        self.rbGaussian = QtGui.QRadioButton(self.groupBox_2)
        self.rbGaussian.setObjectName(_fromUtf8("rbGaussian"))
        self.verticalLayout_4.addWidget(self.rbGaussian)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.slWindowSize = QtGui.QSlider(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slWindowSize.sizePolicy().hasHeightForWidth())
        self.slWindowSize.setSizePolicy(sizePolicy)
        self.slWindowSize.setMinimumSize(QtCore.QSize(150, 0))
        self.slWindowSize.setMinimum(1)
        self.slWindowSize.setMaximum(100)
        self.slWindowSize.setOrientation(QtCore.Qt.Horizontal)
        self.slWindowSize.setObjectName(_fromUtf8("slWindowSize"))
        self.horizontalLayout_2.addWidget(self.slWindowSize)
        self.lbWindowSize = QtGui.QLabel(self.groupBox_2)
        self.lbWindowSize.setObjectName(_fromUtf8("lbWindowSize"))
        self.horizontalLayout_2.addWidget(self.lbWindowSize)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 887, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.slWindowSize, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.lbWindowSize.setNum)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.doOpen)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.doSave)
        QtCore.QObject.connect(self.slWindowSize, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.doUpdateWindowSize)
        QtCore.QObject.connect(self.rbMedian, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.doProcess)
        QtCore.QObject.connect(self.rbGaussian, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.doProcess)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "GPS Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "File info", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Current File:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbFileName.setText(QtGui.QApplication.translate("MainWindow", "No file loaded", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Ascent:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbAscent.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Points:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbPoints.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Descent:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbDescent.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Save as", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Filter options", None, QtGui.QApplication.UnicodeUTF8))
        self.rbMedian.setText(QtGui.QApplication.translate("MainWindow", "Median", None, QtGui.QApplication.UnicodeUTF8))
        self.rbGaussian.setText(QtGui.QApplication.translate("MainWindow", "Gaussian", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Window size", None, QtGui.QApplication.UnicodeUTF8))
        self.lbWindowSize.setText(QtGui.QApplication.translate("MainWindow", "XX", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setText(QtGui.QApplication.translate("MainWindow", "Save As..", None, QtGui.QApplication.UnicodeUTF8))

from graph import Graph
