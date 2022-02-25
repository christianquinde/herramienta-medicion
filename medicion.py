# -*- coding: utf-8 -*-

import sys, math, os, time, subprocess, threading
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *  
from PyQt5.QtWidgets import *

pwd = os.getcwd()

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("medicion.ui",self)
        self.Btn_sincronizar.clicked.connect(self.sync)
        self.Btn_capturar.clicked.connect(self.cap)
        self.Btn_stop.clicked.connect(self.stop)
        self.Btn_metrics.clicked.connect(self.metrics)
        self.Btn_promediar.clicked.connect(self.promediar)
        self.Btn_cargar.clicked.connect(self.cargar)
        self.photo1.setPixmap(QtGui.QPixmap("cuenca.png"))
        self.photo2.setPixmap(QtGui.QPixmap("cuenca.png"))


    def cargar(self):
        global ip_dst, ip_src, piso , trans, tx_rx
        ip_dst = self.ip_dst.text()
        ip_src = self.ip_src.text()
        piso = self.select_piso.currentItem().text()
        trans = self.select_tx.currentItem().text()
        tx_rx = self.select_txorx.currentItem().text()

    def sync(self):
        self.mensaje.setText("Sincronizando ....")
        global ip_dst, ip_src, piso , trans
        ip_dst = self.ip_dst.text()
        ip_src = self.ip_src.text()
        os.chdir(str(pwd)+'/Herramienta')
        subprocess.run(['./sync.sh',str(ip_dst)])




    def cap(self):
        global ip_dst, ip_src, piso , trans, tx_rx
        ip_dst = self.ip_dst.text()
        ip_src = self.ip_src.text()
        piso = self.select_piso.currentItem().text()
        trans = self.select_tx.currentItem().text()
        tx_rx = self.select_txorx.currentItem().text()
        self.mensaje.setText("Capturando ....")
        print(str(ip_dst)+" "+str(ip_src)+" "+str(piso)+" "+str(trans))
        os.chdir(str(pwd)+'/Herramienta/tx')
        subprocess.run(['./captura.sh',str(ip_dst),str(ip_src)])


    def stop(self):
        os.chdir(str(pwd)+'/Herramienta/tx')
        self.mensaje.setText("Captura detenida ....")
        subprocess.run(['./kill.sh',str(piso), str(trans),str(ip_src),str(ip_dst),str(tx_rx)])



    def metrics(self):
        self.mensaje.setText("Calculando ....")
        os.chdir(pwd+'/Herramienta/tx')
        subprocess.run(['./throughput.sh',str(piso),str(trans)])
        os.chdir(str(pwd)+'/Herramienta')
        pl=subprocess.run(['python3','pl.py',str(piso), str(trans),str("tx/fraction_loss")],capture_output=True) #   'python', 'somescript.py', somescript_arg1, somescript_val1,...]
        pl2=subprocess.run(['python3','pl.py',str(piso), str(trans),str("tx/fraction_loss_audio")],capture_output=True) #   'python', 'somescript.py', somescript_arg1, somescript_val1,...]
        
        throu=subprocess.run(['python3','throughput.py',str(piso), str(trans),str("tx/throughput")],capture_output=True)
        throu2=subprocess.run(['python3','throughput.py',str(piso), str(trans),str("tx/throughput_audio")],capture_output=True)
        
        delay1=subprocess.run(['python3','delay.py',str(piso), str(trans),str("tx/delay")],capture_output=True)
        delay2=subprocess.run(['python3','delay.py',str(piso), str(trans),str("tx/delay_audio")],capture_output=True)


        os.chdir('..')
        print('throu='+str(throu))
        print('throu_audio='+str(throu2))
        print('pl='+str(pl))
        print('pl_audio='+str(pl2))
        print('delay='+str(delay1))
        print('delay_audio='+str(delay2))
        aaa=pl.stdout.decode()
        aaa2=pl2.stdout.decode()
        bbb=throu.stdout.decode()
        bbb2=throu2.stdout.decode()
        ccc=delay1.stdout.decode()
        ccc2=delay2.stdout.decode()
        self.thr_label.setText(bbb)
        self.thr_label_2.setText(bbb2)
        self.delay_label.setText(ccc)
        self.delay_label_2.setText(ccc2)
        self.photo2.setPixmap(QtGui.QPixmap(str(pwd)+"/Herramienta/figuras_throu_audio/"+str(piso)+"_tx"+str(trans)+".png"))
        self.photo1.setPixmap(QtGui.QPixmap(str(pwd)+"/Herramienta/figuras_throu/"+str(piso)+"_tx"+str(trans)+".png"))
        self.pl_label.setText(aaa)
        self.pl_label_2.setText(aaa2)



    def promediar(self):
        os.chdir(str(pwd)+'/Herramienta')
        pl=subprocess.run(['python3','pl_comp.py',str("tx/fraction_loss")],capture_output=True) #   'python', 'somescript.py', somescript_arg1, somescript_val1,...]
        pl2=subprocess.run(['python3','pl_comp.py',str("tx/fraction_loss_audio")],capture_output=True) #   'python', 'somescript.py', somescript_arg1, somescript_val1,...]
        
        throu=subprocess.run(['python3','throughput_comp.py',str("tx/throughput")],capture_output=True)
        throu2=subprocess.run(['python3','throughput_comp.py',str("tx/throughput_audio")],capture_output=True)
        
        delay1=subprocess.run(['python3','delay_comp.py',str("tx/delay")],capture_output=True)
        delay2=subprocess.run(['python3','delay_comp.py',str("tx/delay_audio")],capture_output=True)


#---------------------main-----------------------------------
if __name__ == '__main__':
    #Inicia la aplicacion para abrirla y cerrarla
    app = QApplication(sys.argv)
    GUI = Ui_MainWindow()
    #Muestra nuestra aplicacion
    GUI.show()
    #Cierra nuestra aplicacion cuando le damos a cerrar
    sys.exit(app.exec_())