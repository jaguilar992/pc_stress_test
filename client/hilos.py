import random as rnd
from time import sleep
from requests import post
from threading import Thread

class hilo(Thread):
  def __init__(self):
    Thread.__init__(self)
  def run(self):
    while True:
      num = rnd.randint(1000,2000)
      print num,
      print post("http://127.0.0.1/primo.php", data={"valor":num}).content
      sleep(0.1)

hilos = []
for i in range(20):
  hilos.append(hilo())

for hilo in hilos:
  hilo.start()
