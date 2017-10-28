#!/usr/bin/python3

import sys, math
from PyQt5 import QtCore, uic, QtWidgets
 
# Cargar nuestro archivo .ui en misma carpeta de archivo.py 
form_class = uic.loadUiType("factcalc.ui")[0]
 
class MyWindowClass(QtWidgets.QMainWindow, form_class):
  def __init__(self, parent=None):
    QtWidgets.QMainWindow.__init__(self, parent)
    self.setupUi(self)
    self.calc.clicked.connect(self.calc_clicked)
  

 # boton btn calc
  def calc_clicked(self):
      a = float(self.vein.text())  #toma el dato ingresado por el usuario
      b = float(self.veintc.text())
      c = float(self.trein.text())
      d = float(self.tax.text())
      
#hace el calculo tomando el dato de a,b,c y d
      f = round(20 * a) 
      g = round(25 * b) 
      h = round(35 * c) 
      i = round(25 * d) 

      result = round(f+g+h+i)
      resultf = round(a+b+c+d)
      
#muestra la informacion obtenida en el cuadro td,tf,vein_1,veintc_1,trein_1 y tax_1
      self.td.setText(str(result))  
      self.tf.setText(str(resultf))  
      self.vein_1.setText(str(f))
      self.veintc_1.setText(str(g))
      self.trein_1.setText(str(h))
      self.tax_1.setText(str(i))
 
 
 
app = QtWidgets.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()
