# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:11:47 2020

@author: Abhilash
"""

from os import listdir

import os



def list_of_files(dir_name,fileextension):
    #listnew = []
    print(dir_name,fileextension)
    return (([f for f in listdir(dir_name) if f.endswith(str(fileextension))]))
      
    
    
    

def list_all_files(dir_name,fileextension):

    Allfiles = []
    for dirname, dirs, files in os.walk(dir_name):
#        for filename in files:
        for f in listdir(dirname):
            if f.endswith(str(fileextension)):
                
                Allfiles.append(f)
    return Allfiles
