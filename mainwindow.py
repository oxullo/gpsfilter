#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui

import parser
import filter

class MainWindow(QtGui.QMainWindow):
    def doOpen(self):
        rawValues = parser.load(None)
        processedValues = filter.apply(rawValues, self.slWindowSize.value())
        
        self.graphInput.setValues(rawValues)
        self.graphOutput.setValues(processedValues)

    def doSave(self):
        print 'Save'
