import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os, glob, stat
import pydicom
import pydicom.filewriter as fw
import pylab as pl
import sys
import matplotlib.path as mplPath
from tkinter import *
from tkinter import ttk
matplotlib.use("TkAgg")

# 3. Get all DICOM attributes
def elementdicts(datasets):
    elements = {}
    private_elem = {}
    for dataset in datasets:
        for data_element in dataset:
            if data_element.name not in elements:
                elements[data_element.name] = data_element.repval
            if data_element.name in elements:
                if elements[data_element.name] != data_element.repval:
                    elements[data_element.name] += ", " + data_element.repval
            if data_element.tag.is_private and not data_element.name in private_elem:
                private_elem[data_element.name] = data_element.repval
            if data_element.name in private_elem:
                if private_elem[data_element.name] != data_element.repval:
                    private_elem[data_element.name] += ", " + data_element.repval

    # print("All Dicom Elements")
    # print ("{:<40} {:<40}".format('KEY', 'VALUE'))
    # for key, value in elements.items():
    #     print ("{:<40} {:<40}".format(key, value[0:64]))
    print("Private Dicom Elements")
    print ("{:<40} {:<40}".format('KEY', 'VALUE'))
    for key, value in private_elem.items():
        print ("{:<40} {:<40}".format(key, value[0:64]))
    print ("{:<40} {:<40}".format('----------------', '----------------'))

    return elements, private_elem
