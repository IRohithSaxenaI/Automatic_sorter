from os import listdir
from os.path import join,isfile
import os
import shutil

file_path = r"E:\5th sem"
files=[f for f in listdir(file_path) if isfile(join(file_path,f))]
filelist=[]
filetype_dict={}
for f in files:
    filetype=f.split(".")[1]
    if filetype not in filelist:
        new_folder_name=file_path+"/"+filetype+"_folder"
        filelist.append(filetype)
        filetype_dict[str(filetype)]=str(new_folder_name)
        if not os.path.isdir(new_folder_name):
            os.mkdir(new_folder_name)

i=1
for f in files:
    filetype=f.split(".")[1]
    src_path=file_path+"/"+f
    if filetype in filetype_dict.keys():
        dest_path=filetype_dict[str(filetype)]
        shutil.move(src_path,dest_path)
    print("move %s to %s"%(src_path,dest_path))
    i=i+1
