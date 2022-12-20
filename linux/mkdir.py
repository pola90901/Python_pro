import os
os.system("echo hello terminal command mkdir should work")
y=os.popen("mkdir")#excute mkdir command
y=y.read()
print(y)

