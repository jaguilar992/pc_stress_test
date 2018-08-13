import psutil as ps

list = ps.net_connections(kind="tcp")
for con in list:
   print con
