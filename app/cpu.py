import psutil as ps
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
  
  def enciende_nucleo (self, n):
    if (n<self.numero_nucleos and n!=0):
      return sp.call(self.enceder % ("cpu"+str(n)), shell=True)
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
        return c[0][:-1]=='0'
      else:
        return True

  def get_lista_apagados(self):
    apagados = []
    for nucleo in self.nucleos:
      if (self.esta_apagado(nucleo[3:])):
        apagados.append(nucleo)
    return apagados
  
  def get_lista_encendidos(self):
    encendidos = []
    for nucleo in self.nucleos:
      if (not self.esta_apagado(nucleo[3:])):
        encendidos.append(nucleo)
    return encendidos
    
  def get_porcentaje_n(self,n):
    if (n<self.numero_nucleos):
      try:
        return ps.cpu_percent(percpu=True)[int(n)] or 0
      except Exception as e:
        return 0
    else:
      return 0
        
  def get_clients(self):
    a = ps.net_connections(kind="tcp")
    count = 0
    for con in a:
      if (con.laddr.port==80 and con.raddr and con.status =='ESTABLISHED'):
#      if (con.laddr.port==80):
        count+=1
    return count

if __name__ == '__main__':
  p = Procesador()
  #p.enciende_todos()
  print p.get_lista_apagados()
  print p.get_lista_encendidos()
  print p.get_porcentaje_n(0)
  print p.get_clients()
