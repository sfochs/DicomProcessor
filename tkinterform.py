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

# 5. Form for changing values with tkinter
def tkinterform(elements):
    fields = []
    for key, value in elements.items():
        fields.append(key)
    entryboxes = []
    final_values = {}

    root = Tk()
    root.title("DICOM Value Editor")
    root.geometry("800x800")
    container = Frame(root, width=800, height=800)
    canvas = Canvas(container)
    scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, width=800, height=800)
    scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    def makeform(root, fields):
       entries = {}
       for field in fields:
          row = Frame(scrollable_frame)
          lab = Label(row, width=40, text=field+": ", anchor='w')
          ent = Entry(row, width=50)
          entryboxes.append(ent)
          ent.insert(0, elements[field])
          row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
          lab.pack(side = LEFT)
          ent.pack(side = RIGHT, expand = YES, fill = X)
          entries[field] = ent
       return entries

    def save():
        index = 0
        print("Saved Dicom Elements")
        print ("{:<40} {:<40}".format('KEY', 'VALUE'))
        for ent in entryboxes:
            entered_val = ent.get()
            print ("{:<40} {:<40}".format(fields[index], entered_val[0:64]))
            final_values[fields[index]] = entered_val
            index = index + 1
        print ("{:<40} {:<40}".format('----------------', '----------------'))

    ents = makeform(root, fields)
    bquit = Button(root, text = 'Quit', command = root.quit)
    bquit.pack(side = "bottom", padx = 5, pady = 5)
    bok = Button(root, text = 'Save', command = save)
    bok.pack(side = "bottom", padx = 5, pady = 5)

    container.pack(expand = True, fill = "both")
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()

    return final_values
