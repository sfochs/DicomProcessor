import os, glob
import pydicom

# 2. Extract out DICOM data
def getdatasets(datadirs, plots, names):
    datasets = []
    emptyfiles = []
    for dcmdir in datadirs:
        plot = []
        print("Now traversing" + dcmdir)
        for f in glob.glob(dcmdir + '/*'):
            if not os.path.isdir(f):
                filename = dcmdir + "/" + f.split("/")[-2] + "/" + f.split("/")[-1]
                ds = pydicom.dcmread(f)
                ds.add_new([0x0009, 0x103e], 'SH', dcmdir)

                # only append non-empty datasets
                try:
                    pix = ds.pixel_array
                    pix = pix*1+(-1024)
                    plot.append(pix)
                    datasets.append(ds)
                except Exception as e:
                    emptyfiles.append(filename)
                    print("File " + filename + " is empty. Omitting from datasets[]")

        # only append non-empty plots
        if (len(plot) > 0):
            plots.append(plot)
            names.append(dcmdir)

    return datasets, plots, emptyfiles
