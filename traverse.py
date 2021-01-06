import os, glob
import pydicom

# data from: https://www.dicomlibrary.com/?manage=1b9baeb16d2aeba13bed71045df1bc65
# pydicom man pages: https://pydicom.github.io/pydicom/stable/index.html


# 1. Traverse all folders and subfolders of the given filepath and check which contain .dcm files
def traverse(fpath):
    alldirs = []
    [alldirs.append(x[0]) for x in os.walk(fpath)]
    datadirs = [] # directories in fpath with .dcm files
    for d in alldirs: # print all of the directories, first is current directory
        for f in glob.glob(d + '/*'):
            try:
                if not os.path.isdir(f):
                    pydicom.dcmread(f)
                    d = d.replace("\\", "/")
                    datadirs.append(d)
                    break
            except:
                pass
    return datadirs
