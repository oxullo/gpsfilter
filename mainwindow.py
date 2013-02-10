#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PyQt4 import QtGui

import mainwindow_ui
import fileio
import filter

class MainWindow(QtGui.QMainWindow):
    def __init__(self, *args, **kargs):
        super(MainWindow, self).__init__(*args, **kargs)
        self.ui = mainwindow_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lbWindowSize.setText(str(self.ui.slWindowSize.value()))
        self.__rawValues = None
        self.__resetFileInfo()

    def doOpen(self):
        self.__resetFileInfo()
        fileName = unicode(QtGui.QFileDialog.getOpenFileName())
        try:
            self.__rawValues = fileio.load(fileName)
        except Exception, e:
            msg = QtGui.QMessageBox()
            msg.setText('Error while loading file: %s (%s)' % (fileName, str(e)))
            msg.exec_()
            
        self.ui.lbFileName.setText(os.path.basename(fileName))
        self.ui.lbPoints.setText(str(len(self.__rawValues)))
        self.ui.statusBar.showMessage('Opened file %s' % fileName)
        self.ui.graph.setInputValues(self.__rawValues)
        self.ui.pushButton_2.setEnabled(True)
        self.doProcess()

    def doProcess(self):
        if self.ui.rbMedian.isChecked():
            func = filter.applyMedian
        else:
            func = filter.applyGaussian

        processedValues = func(self.__rawValues, self.ui.slWindowSize.value())
        
        diffs = [processedValues[i+1] - processedValues[i]
                for i in xrange(len(processedValues) - 1)]

        ascensionSegs = [asc for asc in diffs if asc > 0]
        discensionSegs = [dis for dis in diffs if dis < 0]
        
        self.ui.lbAscent.setText('%.2fm' % sum(ascensionSegs))
        self.ui.lbDescent.setText('%.2fm' % sum(discensionSegs))
        self.__processedValues = processedValues
        self.ui.graph.setOutputValues(processedValues)

    def doSave(self):
        fileio.save(self.__processedValues, unicode(QtGui.QFileDialog.getSaveFileName()))

    def doUpdateWindowSize(self, value):
        self.doProcess()

    def __resetFileInfo(self):
        self.ui.lbFileName.setText('No file loaded')
        self.ui.lbPoints.setText('')
        self.ui.lbAscent.setText('')
        self.ui.lbDescent.setText('')

