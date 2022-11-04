import os
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QApplication, QFileDialog, QLineEdit, QLabel
from PyQt6 import QtGui
from PyQt6.QtCore import pyqtSignal
from os.path import dirname
import main as m
import vAffiche
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class vMain(QWidget):
    
    def  __init__(self):
        super().__init__()
        
        self.setWindowTitle('SAE C2') 
        
        self.chemins = []
        #----------------- LAYOUTS -----------------
        self.topLayout : QVBoxLayout = QVBoxLayout() ; self.setLayout(self.topLayout)
        self.ouvrirPhotoLayout : QHBoxLayout = QHBoxLayout()
        self.afficherPhotoLayout : QHBoxLayout = QHBoxLayout()
        #---
        self.graphLayout : QHBoxLayout = QHBoxLayout()
        #---
        self.boutonMoyLayout : QVBoxLayout = QVBoxLayout()
        self.boutonMedLayout : QVBoxLayout = QVBoxLayout()
        self.boutonOutLayout : QVBoxLayout = QVBoxLayout()
        #---          
        self.saveLayout : QHBoxLayout = QHBoxLayout()
        #----------------- CONTAINERS -----------------
        self.cOuvrirPhotoLayout : QWidget = QWidget() ; self.cOuvrirPhotoLayout.setLayout(self.ouvrirPhotoLayout)
        #---
        self.cAfficherPhotoLayout : QWidget = QWidget() ; self.cAfficherPhotoLayout.setLayout(self.afficherPhotoLayout)
        #---
        self.cGraphLayout : QWidget = QWidget() ; self.cGraphLayout.setLayout(self.graphLayout)
        #---
        self.cboutonMoyLayout : QWidget = QWidget() ; self.cboutonMoyLayout.setLayout(self.boutonMoyLayout)
        self.cboutonMedLayout : QWidget = QWidget() ; self.cboutonMedLayout.setLayout(self.boutonMedLayout)
        self.cboutonOutLayout : QWidget = QWidget() ; self.cboutonOutLayout.setLayout(self.boutonOutLayout)
        #---          
        self.cSaveLayout : QWidget = QWidget() ; self.cSaveLayout.setLayout(self.saveLayout)
        #----------------- PLACEMENT PHASE LAYOUTS -----------------
        self.topLayout.addWidget(self.cOuvrirPhotoLayout)
        #---
        self.topLayout.addWidget(self.cAfficherPhotoLayout)
        #---
        self.topLayout.addWidget(self.cGraphLayout)
        #---
        self.topLayout.addWidget(self.cboutonMoyLayout)
        self.topLayout.addWidget(self.cboutonMedLayout)
        self.topLayout.addWidget(self.cboutonOutLayout)  
        #---          
        self.topLayout.addWidget(self.cSaveLayout)
        #----------------- LES BOUTONS -----------------
        self.ouvrirPhotos : QPushButton = QPushButton("Ouvrir les photos 🗂️")
        #---
        self.afficherPhotos : QPushButton = QPushButton("Afficher les images")
        #---
        self.boutonMoy : QPushButton = QPushButton("Empilement par moyenne")
        self.boutonSaveMoy : QPushButton = QPushButton("Sauvegarder l'image 📥")      
        #---   
        self.boutonMed : QPushButton = QPushButton("Empilement par médiane")
        self.boutonSaveMed : QPushButton = QPushButton("Sauvegarder l'image 📥")   
        #---      
        self.boutonOutliers : QPushButton = QPushButton("Empilement par rejet des outliers")  
        self.boutonSaveOut : QPushButton = QPushButton("Sauvegarder l'image 📥")   
        #----------------- PLACEMENT PHASE BOUTONS -----------------
        self.ouvrirPhotoLayout.addWidget(self.ouvrirPhotos)
        #---
        self.afficherPhotoLayout.addWidget(self.afficherPhotos)
        #---
        self.boutonMoyLayout.addWidget(self.boutonMoy)
        self.boutonMoyLayout.addWidget(self.boutonSaveMoy)
        #---
        self.boutonMedLayout.addWidget(self.boutonMed)
        self.boutonMedLayout.addWidget(self.boutonSaveMed)
        #---
        self.boutonOutLayout.addWidget(self.boutonOutliers)
        self.boutonOutLayout.addWidget(self.boutonSaveOut)  
        #----------------- VOILA -----------------
        self.show() #INDISPENSABLE
        #----------------- CALLBACK -----------------
        self.ouvrirPhotos.clicked.connect(self.cbOuvrir)
        #---
        self.afficherPhotos.clicked.connect(self.cbAfficher)
        #---
        self.boutonMoy.clicked.connect(self.cbMoyenne)
        self.boutonMed.clicked.connect(self.cbMediane)
        self.boutonOutliers.clicked.connect(self.cbOutliers)
        #---          
        self.boutonSaveMoy.clicked.connect(self.cbSaveMoy)
        self.boutonSaveMed.clicked.connect(self.cbSaveMed)
        self.boutonSaveOut.clicked.connect(self.cbSaveMed)
        
    def cbMoyenne(self):
        for i in range(len(self.chemins)):
            m.moyenne(self.chemins[i][0])
            
    def cbMediane(self):
        for i in range(len(self.chemins)):
            m.median(self.chemins[i][0])
    
    def cbOutliers(self):
        print("-- TQT FRR CA MARCHE --")
        
    def cbOuvrir(self):
        self.path = QFileDialog.getOpenFileNames( self, "Ouvrir", dirname( __file__ ), "Fichier FITS ( *.fits )" )
        self.chemins.append(self.path)
        
        print(self.chemins)
        print(self.path)
        
    def cbAfficher(self):
        self.vueAffiche : vAffiche.vAffiche = vAffiche.vAffiche(self.chemins)
        print(self.chemins)
        
        
    def cbSaveMoy(self):
        fig = plt.figure()
        for i in range(len(self.chemins)):
            fig = plt.figure(m.moyenne(self.chemins[i][0]))
        plt.ion()
        plt.title("EmpilementParMoyenne")
        plt.close(fig)
        plt.savefig("EmpilementParMoyenne.png")
        
    def cbSaveMed(self):
        fig = plt.figure()
        for i in range(len(self.chemins)):
            fig = plt.figure(m.median(self.chemins[i][0]))
        plt.ion()
        plt.title("EmpilementParMediane")
        plt.close(fig)
        plt.savefig("EmpilementParMediane.png")
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w0 : vMain = vMain()
    sys.exit(app.exec()) 