import subprocess as sp
import os
import re

# Gestion de nucleos del procesador
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
    if (n<self.numero_nucleos and n!=0):
      return sp.call(self.apagar % ("cpu"+str(n)), shell=True)
    else:
      return None
  
  def esta_apagado(self, n):
    n = int(n)
    if (n==0):
      return False
    else:
      if (n<self.numero_nucleos):
        f = open('/sys/devices/system/cpu/cpu%s/online' % n, 'r')
        c = f.readlines()
        f.close()
        print c[0][:-1]==1
        return c[0][:-1]==1
      else:
        return True

  def get_lista_apagados(self):
    apagados = []
    for nucleo in self.nucleos:
      print nucleo[3:]
      if (self.esta_apagado(nucleo[3:])):
        apagados.append(nucleo)
    return apagados
  
  def get_lista_encendidos(self):
    apagados = self.get_lista_apagados()

        
      

if __name__ == '__main__':
  p = Procesador()
  p.apaga_todos()
  print p.get_lista_apagados()