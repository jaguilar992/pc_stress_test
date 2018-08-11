import subprocess as sp
import os
import re

class Procesador():
  def __init__(self):
    self.nucleos = []
    self.numero_nucleos = self.cuenta_nucleos()
    self.enceder = 'echo 1 | sudo tee /sys/devices/system/cpu/%s/online'    
    self.apagar = 'echo 0 | sudo tee /sys/devices/system/cpu/%s/online'

  def cuenta_nucleos(self):
    folder = os.listdir('/sys/devices/system/cpu/')
    self.nucleos = re.findall(r"cpu[0-9]+", "".join(folder))
    return len(self.nucleos)

  def enciende_todos(self): 
    for nucleo in self.nucleos:
      if nucleo != 'cpu0':
        sp.call(self.enceder % nucleo, shell=True)
  
  def apaga_todos(self):
    for nucleo in self.nucleos:
        if nucleo != 'cpu0':
          sp.call(self.apagar % nucleo, shell=True)
  
  def apaga_nucleo (self, n):
    if (n<self.cuenta_nucleos and n!=0):
      return sp.call(self.apagar % n, shell=True)

if __name__ == '__main__':
  p = Procesador()
  p.apaga_todos()