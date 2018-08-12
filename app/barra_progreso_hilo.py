import time
from PyQt5 import QtCore
class BarraProgresoHilo(QtCore.QThread):
  def __init__(self, bar,cpu, n):
    QtCore.QThread.__init__(self)
    self.n = n
    self.cpu = cpu
    self.bar = bar
  
  def run(self):
    while True:
      self.bar.setValue(self.cpu.get_porcentaje_n(self.n))
      time.sleep(0.25)
    