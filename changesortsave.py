import os, glob
import pydicom
import pydicom.filewriter as fw

# 6. Change datasets based on user-given alterations
def changesortsave(datadirs, alterations, emptyfiles):
    for dcmdir in datadirs:
        print("Now traversing" + dcmdir)
        slices = []
        fn = None
        first = 0
        for f in glob.glob(dcmdir + '/*'):
            if not os.path.isdir(f):
                fn = f
                filename = dcmdir + "/" + f.split("/")[-2] + "/" + f.split("/")[-1]

                if (not filename in emptyfiles):
                    # read each of the dcm files and add them to a list
                    ds = pydicom.dcmread(f)

                    # Change ds via alterations
                    for data_element in ds:
                        if data_element.name in alterations:
                            # print("modifying " + data_element.name + " from " +  data_element.repval + " to " + alterations[data_element.name])
                            data_element.value = alterations[data_element.name]

                    if first == 0:
                        first = ds
                    slice = [ds, f]
                    slices.append(slice)
                else:
                    print("skipping " + filename)

        # 7. Sort by DICOM Image Position (Patient) coordinates
        if(first != 0): #ignore if empty folder
            differenceX = abs(first.ImagePositionPatient[0] - ds.ImagePositionPatient[0])
            differenceY = abs(first.ImagePositionPatient[1] - ds.ImagePositionPatient[1])
            differenceZ = abs(first.ImagePositionPatient[2] - ds.ImagePositionPatient[2])

            if (differenceX >= differenceY) and (differenceX >= differenceZ):
                largest = 0
            elif (differenceY >= differenceX) and (differenceY >= differenceZ):
                largest = 1
            else:
                largest = 2

            slices = sorted(slices, key=lambda s: s[0][0x20,0x32].value[largest])

            # 8. Save new, altered DICOM files
            parentdir = dcmdir.split(fn.split("/")[-2])[0] # parent directory
            newdir = "sorted-" + fn.split("/")[-2]
            print("created: " + newdir)
            os.mkdir(parentdir + newdir, 0o777)
            imagenum = 1
            for s in slices:
                if imagenum < 10:
                    fw.dcmwrite(parentdir + newdir + "/image-00" + str(imagenum) + ".dcm", s[0])
                elif imagenum < 100:
                    fw.dcmwrite(parentdir + newdir + "/image-0" + str(imagenum) + ".dcm", s[0])

                imagenum = imagenum + 1
