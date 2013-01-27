#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import scipy.ndimage

def applyGaussian(values, window):
    return list(scipy.ndimage.filters.gaussian_filter(numpy.array(values), window))

def applyMedian(values, window):
    return list(scipy.ndimage.filters.median_filter(numpy.array(values), window))
