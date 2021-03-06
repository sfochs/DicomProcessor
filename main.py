from traverse import *
from dicomviewer import *
from getdatasets import *
from elementdicts import *
from tkinterform import *
from changesortsave import *
# data from: https://www.dicomlibrary.com/?manage=1b9baeb16d2aeba13bed71045df1bc65
# pydicom man pages: https://pydicom.github.io/pydicom/stable/index.html

fpath = "/Users/sarahfochs/Desktop/knee2/"

# datadirs is a list of directories with DICOM data
datadirs = traverse(fpath)

plots = []
names = []

# datasets is a list of pydicom dictionaries
datasets, plots, emptyfiles = getdatasets(datadirs, plots, names)

# elements and private_elem are dictionaries of the DICOM pre-edit
elements, private_elem = elementdicts(datasets)


# matplotlib viewer

print("Enter a number to view dicom: ")
print("<ENTER>\t: Skip")
for i in range(0, len(names)):
    print(str(i) + ": " + names[i])

num = input()

if num:
    dicomviewer(plots[int(num)], names[int(num)])


# final_elements is a dictionary of the DICOM post-edit
final = tkinterform(elements)

alterations = {}

print("Edited Dicom Elements")
print ("{:<40} {:<40}".format('KEY', 'VALUE'))
for key, val in (set(final.items())).difference(set(elements.items())):
    alterations[key] = val
    print ("{:<40} {:<40}".format(key, val[0:64]))
print ("{:<40} {:<40}".format('----------------', '----------------'))

changesortsave(datadirs, alterations, emptyfiles)
