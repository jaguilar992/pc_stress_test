import psutil as ps
a = ps.net_connections(kind="tcp")
for con in a:
  if (con.laddr.port==80 and con.raddr and con.status =='ESTABLISHED'):
    print con.raddr

