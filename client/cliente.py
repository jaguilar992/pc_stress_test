url = 'http://192.168.1.6/primo.php'
from threading import Thread
from requests import post
import time
class Cliente(Thread):
    def __init__(self, n):
      Thread.__init__(self)
      self.n = n

    def postear(self, n):
      data = {
        "valor" : n
      }
      return post(url, data=data).content

    def run(self):
      try:
        toc = time.time()
        self.postear(self.n)
        tic = time.time()
      except Exception as e:
        pass
