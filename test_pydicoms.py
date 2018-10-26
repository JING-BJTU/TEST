
# coding: utf-8


import pydicom
import dicom
import tempfile
import os, sys
import pandas as pd
from pandas import Series,DataFrame

def PatientNameNiMing(path):
    for root , dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".dcm"):
                dcm = pydicom.dcmread(os.path.join(root, name),force = True)
                dcm.data_element('PatientName').value = dcm.data_element('PatientID').value
                #dcm.data_element('OtherPatientNames').value = dcm.data_element('PatientID').value
                print dcm.data_element('PatientName').value
                if 'OtherPatientNames' in dcm:
                    del dcm.OtherPatientNames
                dcm.save_as(os.path.join(root, name))



#PatientNameNiMing(file_in)


file_patient = '/home/huiying/Documents/data/cui_777/'


patientsIDs = []


def PatientIDs(path):
    for root , dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".dcm"):
                dcm = pydicom.dcmread(os.path.join(root, name),force = True)
                patientID = dcm.data_element('PatientID').value       
                #print patientID
                patientsIDs.append(patientID)
    print patientsIDs
    return patientsIDs


studysUIDs = []


def StudyUIDs(path):
    for root , dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".dcm"):
                dcm = pydicom.dcmread(os.path.join(root, name),force = True)
                studyUID = dcm.data_element('StudyInstanceUID').value       
                studysUIDs.append(studyUID)
    return studysUIDs


studysIDs = []


def StudyIDs(path):
    for root , dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".dcm"):
                dcm = pydicom.dcmread(os.path.join(root, name),force = True)
                studyID = dcm.data_element('StudyID').value       
                studysIDs.append(studyID)
    return studysIDs


studysUIDs = StudyUIDs(file_patient)
print len(studysUIDs)
suid = list({}.fromkeys(studysUIDs).keys())
suid = DataFrame(suid)
print suid
print suid
suid.to_csv('/home/huiying/Documents/data/cui_777_suid.csv', index=False, header=False )
file=open('/home/huiying/Documents/dataq/cui_777_suid.txt','w')
file.write(str(suid));
file.close()


#patientIDs = PatientIDs(file_patient)
print len(patientIDs)
pid = list({}.fromkeys(patientIDs).keys())
#print pid
pid = DataFrame(pid)
print pid
file=open('/home/huiying/Documents/dataq/cui_778_pid.txt','w')
file.write(str(pid));
file.close()



#studysIDs = StudyIDs(file_patient)
print len(studysIDs)
sid = list({}.fromkeys(studysIDs).keys())
#print sid
sid = DataFrame(sid)
print sid
file=open('/home/huiying/Documents/data/cui_778_sid.txt','w')
file.write(str(sid));
file.close()

