# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\ibrahim_ediz\OrtakProje\Ana.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AnaPencere(object):
    def setupUi(self, AnaPencere):
        AnaPencere.setObjectName("AnaPencere")
        AnaPencere.resize(524, 560)
        self.centralwidget = QtWidgets.QWidget(AnaPencere)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 511, 421))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 411))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lblID = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblID.setText("")
        self.lblID.setObjectName("lblID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lblID)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txtAdi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtAdi.setObjectName("txtAdi")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtAdi)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtSoyadi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtSoyadi.setObjectName("txtSoyadi")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtSoyadi)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtTelefon = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtTelefon.setObjectName("txtTelefon")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtTelefon)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.txtPosta = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtPosta.setObjectName("txtPosta")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtPosta)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.cmbIl = QtWidgets.QComboBox(self.formLayoutWidget)
        self.cmbIl.setObjectName("cmbIl")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.cmbIl)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.cmbIlce = QtWidgets.QComboBox(self.formLayoutWidget)
        self.cmbIlce.setObjectName("cmbIlce")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.cmbIlce)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.tblListe = QtWidgets.QTableWidget(self.formLayoutWidget)
        self.tblListe.setObjectName("tblListe")
        self.tblListe.setColumnCount(0)
        self.tblListe.setRowCount(0)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.tblListe)
        self.btKaydet = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btKaydet.setObjectName("btKaydet")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.btKaydet)
        self.btVazgec = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btVazgec.setObjectName("btVazgec")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.btVazgec)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        AnaPencere.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AnaPencere)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 524, 18))
        self.menubar.setObjectName("menubar")
        self.kayit = QtWidgets.QMenu(self.menubar)
        self.kayit.setObjectName("kayit")
        self.telefon = QtWidgets.QMenu(self.kayit)
        self.telefon.setObjectName("telefon")
        AnaPencere.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AnaPencere)
        self.statusbar.setObjectName("statusbar")
        AnaPencere.setStatusBar(self.statusbar)
        self.actionEposta_Listesi = QtWidgets.QAction(AnaPencere)
        self.actionEposta_Listesi.setObjectName("actionEposta_Listesi")
        self.TelEkleme = QtWidgets.QAction(AnaPencere)
        self.TelEkleme.setObjectName("TelEkleme")
        self.TelListeleme = QtWidgets.QAction(AnaPencere)
        self.TelListeleme.setObjectName("TelListeleme")
        self.telefon.addAction(self.TelEkleme)
        self.telefon.addAction(self.TelListeleme)
        self.kayit.addAction(self.telefon.menuAction())
        self.kayit.addAction(self.actionEposta_Listesi)
        self.menubar.addAction(self.kayit.menuAction())

        self.retranslateUi(AnaPencere)
        QtCore.QMetaObject.connectSlotsByName(AnaPencere)

    def retranslateUi(self, AnaPencere):
        _translate = QtCore.QCoreApplication.translate
        AnaPencere.setWindowTitle(_translate("AnaPencere", "Telefon Defteri"))
        self.label_7.setText(_translate("AnaPencere", "Kayıt ID:"))
        self.label.setText(_translate("AnaPencere", "Adı:"))
        self.label_2.setText(_translate("AnaPencere", "Soyadı:"))
        self.label_3.setText(_translate("AnaPencere", "Telefon"))
        self.label_4.setText(_translate("AnaPencere", "E Posta"))
        self.label_5.setText(_translate("AnaPencere", "İLİ"))
        self.label_6.setText(_translate("AnaPencere", "İLÇESİ"))
        self.label_9.setText(_translate("AnaPencere", "  Liste"))
        self.btKaydet.setText(_translate("AnaPencere", "Kaydet"))
        self.btVazgec.setText(_translate("AnaPencere", "Vazgeç"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("AnaPencere", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("AnaPencere", "Tab 2"))
        self.kayit.setTitle(_translate("AnaPencere", "Kayıt"))
        self.telefon.setTitle(_translate("AnaPencere", "Telefon Listesi"))
        self.actionEposta_Listesi.setText(_translate("AnaPencere", "Eposta Listesi"))
        self.TelEkleme.setText(_translate("AnaPencere", "Ekleme"))
        self.TelListeleme.setText(_translate("AnaPencere", "Listeleme"))

