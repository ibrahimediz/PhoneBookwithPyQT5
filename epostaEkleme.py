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
        self.epostaDialog.btKaydet.clicked.connect(self.epostaDialog.close)
    

    # @pyqtSlot(int)
    # def isimdegis(self,val=0):
    #     liste = self.veritabani.TelListe(val)
    #     self.telDialog.listTel.clear()
    #     for item in liste:
    #         self.telDialog.listTel.addItem(item[1])

    #     print(liste)
    # def tetikleme(self,anaMenu=None):
    #     anaMenu.kayitId.connect(self.isimdegis)