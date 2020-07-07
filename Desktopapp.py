# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 00:24:41 2018

@author: Chaitanya
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 14:31:41 2018

@author: Chaitanya
"""

import sys
from PyQt5 import QtGui
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit,QAction,QMessageBox,QCheckBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QComboBox
#from nmt_dfnc_correlation_alldata import train
import GenerateCSVMethods
import pandas as pd
import os

fileName  = ("This is Folder")
fileName1 = ("This is Filetype")


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        


        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("File Selection Type") 

        
        #Configure Analysis Button
        
        pybutton = QPushButton('Generate Csv-Folder', self)
        
        pybutton.resize(200,32)
        pybutton.move(100, 60)     
        pybutton.setToolTip('This is a to generate CSV files')  
        
        #Adding Menu bar
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu = menuBar.addMenu('&Defaults') 
        
        #When Clicked to display Next window
        pybutton.clicked.connect(self.clickMethod)
        self.dialog = secondwindow()
        
        #Setting Defaults
        
        
        #Priniting Global files
        #Run button
        self.Runbutton = QPushButton('Count File type', self)
        self.Runbutton.resize(200,32)
        self.Runbutton.move(100, 100)     
        self.Runbutton.setToolTip('This is a to get the count of file types of same type') 
        
        self.Runbutton.clicked.connect(self.runmethod)
        
        

    def clickMethod(self):
        

         self.dialog.show()
     
    def runmethod(self):
        global fileName
        global fileName1
        files=GenerateCSVMethods.list_all_files(fileName,fileName1)

        files = pd.DataFrame(files)
        filenametobesaved = input("Enter the filename to be saved")
        #indexofcsvfile = input(str("Enter Index of CSV file to be True or False"))
        files.to_csv(filenametobesaved,index=False,index_label=False)

                
        
# Navigating wwindow() 
class secondwindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("Select Folder")
        
        self.DirectoryName = ("")
        #self.fmriName = ("")
        
        global fileName
        global fileName1
        
        
        self.pybutton1 = QPushButton('Select Folder', self)
        self.pybutton1.resize(200,32)
        self.pybutton1.move(100, 60)
        
        self.pybutton3 = QPushButton('Generate Csv with Filenames location', self)
        self.pybutton3.resize(200,32)
        self.pybutton3.move(100, 100)
        self.pybutton3.setToolTip('This is to generate CSV files') 
        self.pybutton3.clicked.connect(self.GCSV)
        
        #self.dropdown = QLabel("DropDown Files", self)
        self.pybutton2 = (QComboBox(self))
        self.pybutton2.addItem(".mp4")
        self.pybutton2.addItem(".txt")
        self.pybutton2.addItem(".pdf")
        self.pybutton2.addItem(".wmv")
        self.pybutton2.addItem(".csv")
        self.pybutton2.addItem(".py")
        
        #self.dropdown.move(650,150)
        self.pybutton2.activated[str].connect(self.onChanged)      
        
        self.setGeometry(50,50,320,200)
        #self.setWindowTitle("QLineEdit Example")
        #self.pybutton2.show()
        
#        fileName1 = 
#        print(fileName1)
        #Browsing Files
        self.pybutton1.clicked.connect(self.Browse)
        #self.pybutton2.clicked.connect(self.Browse1)
        
#        print("self.smri"+self.smriName,"self.fmri"+self.fmriName)
#        
#        fileName = self.smriName
#        fileName1 = self.fmriName
#        
#        print("Filename is"+fileName,"Filename1 is"+fileName1)
        
    def Browse(self):
        
        global  fileName
         
        
        
        #self.smriName,_ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath() , '*')
        self.DirectoryName = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        
        print(self.DirectoryName)
        
        if (len(self.DirectoryName)  == 0):
            QMessageBox.about(self, "Pleae select File Type From the list")
        else:
            
            print("Directory selected")
            self.pybutton1.setStyleSheet("background-color: green")
            
            fileName = self.DirectoryName
            print("Filename is"+fileName)
    def GCSV(self): 
        global fileName
        global fileName1
        print(fileName,fileName1)
        files = GenerateCSVMethods.list_of_files(fileName,fileName1)       
        print(files)
        files = pd.DataFrame(files)
        filenametobesaved = input("Enter the filename to be saved")
        #indexofcsvfile = input(str("Enter Index of CSV file to be True or False"))
        files.to_csv(filenametobesaved,index=False,index_label=False)
    def onChanged(self, text):
        global fileName1
        self.setText = text
        fileName1 = (self.setText)
        print(fileName1)
        
#class thirdwindow(QMainWindow):
#    def __init__(self):
#        QMainWindow.__init__(self)
#
#        self.setMinimumSize(QSize(320, 140))    
#        self.setWindowTitle("Select required Defaults")
        
        
           
        
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

