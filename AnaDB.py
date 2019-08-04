from  DB import DBGenel
import os
class AnaDB(DBGenel):
    def __init__(self):
        super().__init__(os.getcwd() + os.sep+"TDF.db")
        
    def kisiListele(self):
        liste = self.select(TABLO="V_KISI_LISTE",SUTUN=["ID","ADI","SOYADI","ILI","ILCESI"])
        return liste
    def kisiEkle(self,adi,soyadi,il,ilce):
        sonuc = self.insert(TABLO="TDF_DEFTER",DEGER=[("Adi","'"+adi+"'"),("Soyadi","'"+soyadi+"'"),("il",str(il)),("ilce",str(ilce))])
        return sonuc
    def ilListele(self):
        liste = self.select(TABLO="ST_ILLER",SUTUN=["IL_ID","IL_ADI"])
        return liste
    def ilceListe(self,ilID):
        liste = self.select(TABLO="ST_ILCELER",SUTUN=["ILCE_ID","ILCE_ADI"],SART=[("1","IL_ID",str(ilID))])
        return liste
