#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt4 import uic, QtGui

import mainwindow

app = QtGui.QApplication(sys.argv)
mainWindow = uic.loadUi('mainwindow.ui', mainwindow.MainWindow())
mainWindow.show()

sys.exit(app.exec_())
