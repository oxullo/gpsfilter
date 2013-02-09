#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt4 import uic, QtGui

import mainwindow

app = QtGui.QApplication(sys.argv)
mainWindow = mainwindow.MainWindow()
mainWindow.show()
mainWindow.raise_()

sys.exit(app.exec_())
