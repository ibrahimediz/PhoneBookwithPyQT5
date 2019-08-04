import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic,QtGui,QtCore
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QPushButton,QTableWidgetItem
from TelEklemeDB import telEkleme
import os

class TelApp(QWidget):
    #Telefon Menüsü PyQT
    def __init__(self,parent=None):
        super(TelApp, self).__init__(parent)
        self.telDialog = uic.loadUi(os.getcwd() + os.sep+"telEkleme.ui")
        self.veritabani = telEkleme()
        self.initUI()

    def initUI(self):
        self.telDialog.btKaydet.clicked.connect(self.telDialog.close)
    

    @pyqtSlot(int)
    def isimdegis(self,val=0):
        liste = self.veritabani.TelListe(val)
        self.telDialog.listTel.clear()
        for item in liste:
            self.telDialog.listTel.addItem(item[1])

        print(liste)
    def tetikleme(self,anaMenu=None):
        anaMenu.kayitId.connect(self.isimdegis)