import os
os.system("echo hello terminal command hostname should work")
y=os.popen("hostname")#excute hostname command
y=y.read()
print(y)

