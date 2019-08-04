import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic,QtGui,QtCore
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QPushButton,QTableWidgetItem
from epostaDB import epostaEkleme
import os

class EpostaApp(QWidget):
    listeID = ""
    #Eposta Menüsü PyQT
    def __init__(self,parent=None):
        super(EpostaApp, self).__init__(parent)
        self.epostaDialog = uic.loadUi(os.getcwd() + os.sep+"ePostaEkleme.ui")
        self.veritabani = epostaEkleme()
        self.initUI()

    def initUI(self):
        pass
        # self.epostaDialog.btKaydet.clicked.connect(self.epostaDialog.close)
    
    def gosterme(self):
        try:
            self.listeleme(self.listeID)
            self.epostaDialog.show()
        except:
            pass

    
    def listeleme(self,val=0):
        liste = self.veritabani.epostaDB(val)
        self.epostaDialog.listEposta.clear()
        for item in liste:
            self.epostaDialog.listEposta.addItem(item[1])
