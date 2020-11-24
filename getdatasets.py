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

# 2. Extract out DICOM data
def getdatasets(datadirs, plots, names):
    datasets = []
    for dcmdir in datadirs:
        plot = []
        print("Now traversing" + dcmdir)
        for f in glob.glob(dcmdir + '/*'):
            if not os.path.isdir(f):
                ds = pydicom.dcmread(f)
                ds.add_new([0x0009, 0x103e], 'SH', dcmdir)
                datasets.append(ds)

                # print(ds[0x20,0x32].value[2])
                pix = ds.pixel_array
                pix = pix*1+(-1024)
                plot.append(pix)
        plots.append(plot)
        names.append(dcmdir)

    return datasets, plots
