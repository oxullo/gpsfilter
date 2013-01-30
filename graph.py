#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore

class Graph(QtGui.QFrame):
    def __init__(self, *args, **kargs):
        super(Graph, self).__init__(*args, **kargs)
        self.__values = []
        self.__coords = []

    def setValues(self, values):
        self.__values = values
        self.__recalc()
        self.repaint()
        
    def paintEvent(self, event):
        super(Graph, self).paintEvent(event)
        if self.__coords:
            painter = QtGui.QPainter(self)
            painter.setRenderHint(QtGui.QPainter.Antialiasing, True)

            painter.drawPolyline(*self.__coords)

    def __recalc(self):
        xstep = float(self.size().width()) / len(self.__values)
        height = self.size().height()
        maxval = float(max(self.__values))
    
        self.__coords = []
        xpos = 0
        for value in self.__values:
            self.__coords.append(QtCore.QPointF(xpos, (1 - value / maxval) * height))
            xpos += xstep
