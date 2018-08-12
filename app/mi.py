import subprocess
command = 'cat /proc/stat|grep "^cpu[0-9]* "'  # or whatever you use
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate[0]

# parse output here and extract cpu usage. this is super-dependent
# on the layout of your system monitor output
cpuline = output.split('\n')[2]
