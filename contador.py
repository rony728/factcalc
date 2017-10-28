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
  

 # boton btn_Ctof
  def calc_clicked(self):
      a = float(self.vein.text())  #toma el dato ingresado por el usuario
      b = float(self.veintc.text())
      c = float(self.trein.text())
      d = float(self.tax.text())

      f = round(20 * a) #hace el calculo tomando el dato de a
      g = round(25 * b) #hace el calculo tomando el dato de b
      h = round(35 * c) #hace el calculo tomando el dato de c
      i = round(1 * d) #hace el calculo tomando el dato de d
      result = round(f+g+h+i)
      self.td.setText(str(result))  #muestra la informacion obtenida en el cuadro fah
 
 
 
app = QtWidgets.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()
