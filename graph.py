#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure

from PyQt4 import QtGui, QtCore

class MplCanvas(FigureCanvas):
    """Class to represent the FigureCanvas widget"""
    def __init__(self):
        self.fig = Figure()
        self.input = self.fig.add_subplot(211)
        self.output = self.fig.add_subplot(212)
        
        FigureCanvas.__init__(self, self.fig)
        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Expanding)
        self.updateGeometry()


class Graph(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Graph, self).__init__(parent)
        self.canvas = MplCanvas()
        self.navi = NavigationToolbar(self.canvas, self)
        self.vbl = QtGui.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.vbl.addWidget(self.navi)
        self.setLayout(self.vbl)
        
    def setInputValues(self, values):
        self.canvas.input.clear()
        self.canvas.output.clear()
        self.canvas.input.plot(range(0, len(values)), values)
        self.canvas.input.grid()
        self.canvas.draw()

    def setOutputValues(self, values):
        self.canvas.output.clear()
        self.canvas.output.plot(range(0, len(values)), values)
        self.canvas.output.grid()
        self.canvas.draw()
    