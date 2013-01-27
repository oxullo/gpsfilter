#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PyQt4 import QtGui
from PyQt4 import uic

import parser
import filter

class MainWindow(QtGui.QMainWindow):
    def __init__(self, *args, **kargs):
        super(MainWindow, self).__init__(*args, **kargs)
        self.ui = uic.loadUi('mainwindow.ui', self)
        self.__rawValues = None
        self.__resetFileInfo()

    def doOpen(self):
        self.__resetFileInfo()
        fileName = unicode(QtGui.QFileDialog.getOpenFileName())
        try:
            self.__rawValues = parser.load(fileName)
        except Exception, e:
            msg = QtGui.QMessageBox()
            msg.setText('Error while loading file: %s (%s)' % (fileName, str(e)))
            msg.exec_()
            
        self.ui.lbFileName.setText(os.path.basename(fileName))
        self.ui.statusBar.showMessage('Opened file %s' % fileName)
        self.ui.graphInput.setValues(self.__rawValues)
        self.doProcess()

    def doProcess(self):
        if self.ui.rbMedian.isChecked():
            func = filter.applyMedian
        else:
            func = filter.applyGaussian

        processedValues = func(self.__rawValues, self.ui.slWindowSize.value())
        self.ui.graphOutput.setValues(processedValues)

    def doSave(self):
        print 'Save'

    def doUpdateWindowSize(self, value):
        self.doProcess()

    def __resetFileInfo(self):
        self.ui.lbFileName.setText('No file loaded')
        self.ui.lbFileType.setText('')
        self.ui.lbPoints.setText('')

