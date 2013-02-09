#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

setup(
    windows=[{"script" : "gpsfilter.pyw"}],
    options={
        "py2exe" : {
            "includes" : ["sip", ],
            "dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"],
            "bundle_files": 1,
            "compressed": True,
        }},
    zipfile=None)
