from cliente import Cliente
import random as rnd
import time

def test(n):
  clientes = []
  for i in range(n):
    clientes.append(Cliente(10000))
  
  for cliente in clientes:
    cliente.start()

print "Test de Web Service"
num = int(raw_input("Numero de conexiones simultaneas: "))
while num>0:
  print "Creando %s conexiones simultaneas" % num
  test(num)
  num = int(raw_input("Numero de conexiones simultaneas: "))
