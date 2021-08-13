import tarfile
import os

tarFileName= "20210805235343_ucspsimccd008_UCSM.tar"

fileName = "sam_techsupportinfo"


def fileOpen(file):
    fileObj = tarfile.open(file, "r")
    members = fileObj.getmembers()
    fileObj.close()
    return members


def checkFiles(members):
    for member in members:
        if member.name.endswith(fileName):
            print("file exist")
            ### do the operation ###
            
        elif member.name.endswith("tar.gz"):
            chassis = fileOpen(member.name)
            print(type(chassis))
            checkFiles(chassis)
