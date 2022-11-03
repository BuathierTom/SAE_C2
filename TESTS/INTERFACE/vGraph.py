from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QApplication, QFileDialog, QLineEdit, QLabel
from PyQt6.QtCore import pyqtSignal
import vOuvrir 
import main as m

class vGraph(QWidget):
    def  __init__(self):    
        super().__init__()
        #----------------- IMPORT -----------------
        self.vue : vOuvrir.vOuvrir = vOuvrir.vOuvrir() 
        #----------------- LAYOUTS -----------------
        self.topLayout : QVBoxLayout = QVBoxLayout() ; self.setLayout(self.topLayout)
        self.graphLayout : QHBoxLayout = QHBoxLayout()
        self.boutonlayout : QHBoxLayout = QHBoxLayout()
        #----------------- CONTAINERS -----------------
        self.cGraphLayout : QWidget = QWidget() ; self.cGraphLayout.setLayout(self.graphLayout)
        self.cBoutonlayout : QWidget = QWidget() ; self.cBoutonlayout.setLayout(self.boutonlayout)
        #----------------- PLACEMENT PHASE 0 -----------------
        self.topLayout.addWidget(self.cGraphLayout)
        self.topLayout.addWidget(self.cBoutonlayout)
        #----------------- LES BOUTONS -----------------
        self.boutonMoy : QPushButton = QPushButton("Empilement par moyenne")
        self.boutonMed : QPushButton = QPushButton("Empilement par médiane")
        self.boutonOutliers : QPushButton = QPushButton("Empilement par rejet des outliers")
        #----------------- ON PLACE -----------------
        self.boutonlayout.addWidget(self.boutonMoy)
        self.boutonlayout.addWidget(self.boutonMed)
        self.boutonlayout.addWidget(self.boutonOutliers)
        #----------------- VOILA -----------------
        # self.show() #INDISPENSABLE
        #----------------- CALLBACK -----------------
        self.boutonMoy.clicked.connect(self.cbMoyenne)
        self.boutonMed.clicked.connect(self.cbMediane)
        self.boutonOutliers.clicked.connect(self.cbOutliers)
        
    def cbMoyenne(self, chemin: list):
        m.moyenne(chemin)
        
    def cbMediane(self, images: list):
        m.median(images)
    
    def cbOutliers(self, images: list):
        print("-- TQT FRR CA MARCHE --")
        
        
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w0 : vGraph = vGraph()
    sys.exit(app.exec()) 