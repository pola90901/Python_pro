import os
os.system("echo hello terminal command LS should work")
y=os.popen("ls")#excute ls command
y=y.read()
print(y)

