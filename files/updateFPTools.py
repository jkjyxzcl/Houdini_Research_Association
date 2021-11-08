# -*- coding: UTF-8 -*-
# @Author : -k-
# @Time   : 2021/11/02

import os
import sys
import shutil 
import maya.cmds as cmds
import maya.mel as mel

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

def updateFile(file,old_str,new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w") as f:
        f.write(file_data)

def make_folder(dir):
    folder = os.path.exists(dir)

    if folder:
        # shutil.rmtree(dir)
        pass
    else:
        os.makedirs(dir)
    return dir
    
def update_tools():
    nas_path = '//nass.funplus.io/PuzzleMarketADS/update_tools/maya/'
    scripts_path = os.path.join(nas_path, 'scripts')
    shelves_path = os.path.join(nas_path, 'shelves')
    
    file_scripts_list = os.listdir(scripts_path)
    file_shelves_list = os.listdir(shelves_path)
    
    
    maya_path = mel.eval('getenv("MAYA_APP_DIR")')

    tar_scripts_path = os.path.join(maya_path, 'scripts/FpHlw')
    make_folder(tar_scripts_path)
    tar_shelves_path = os.path.join(maya_path, '2019/prefs/shelves')
    # cmds.confirmDialog(message='{}'.format(tar_scripts_path), button=["ok"])
    # shutil.copytree(scripts_path,tar_shelves_path)

    for file in file_scripts_list:
        # print(file)
        file_path = os.path.join(scripts_path,file)
        if os.path.isdir(file_path):
            sub_file_list = os.listdir(file_path)
            sub_tar_path = os.path.join(tar_scripts_path,file)
            make_folder(sub_tar_path)
            for sub_file in sub_file_list:
                sub_src_path = os.path.join(file_path,sub_file)
                sub_file_tar_path = os.path.join(sub_tar_path,sub_file)
                shutil.copyfile(sub_src_path, sub_file_tar_path)
        else:
            shutil.copyfile(file_path,os.path.join(tar_scripts_path, file))

    for file in file_shelves_list:
        file_path = os.path.join(shelves_path,file)
        tar_path = os.path.join(tar_shelves_path, file)
        cmds.quit()
        shutil.copyfile(file_path,tar_path)


        