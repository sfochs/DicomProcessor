# DicomProcessor
Given an architecture of directories and DICOM Images: 

(1) Identify all DICOM file directories
* DICOMs do are not required to have .dcm extension
    
(2) extract out DICOM data with pydicom

(3) visualize DICOMs with matplotlib

(4) edit DICOM elements with tkinter

(5) save and apply changes throughout all DICOMS
* edited files are saved as new files with a .dcm extension
* new files are saved in new folders with prefix "sorted-" under the same parent folder
