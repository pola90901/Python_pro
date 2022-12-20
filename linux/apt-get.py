import os
os.system("echo hello terminal command apt-get should work")
y=os.popen("apt-get")#excute apt-get command
y=y.read()
print(y)

