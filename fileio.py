#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

def load(file):
    reader = csv.reader(open(file), delimiter='\t')
    
    data = []
    for row in reader:
        print row
        try:
            lev = float(row[0].replace(',', '.'))
        except ValueError:
            print 'Cannot parse height %s' % row[0]
        else:
            data.append(lev)
    
    return data
