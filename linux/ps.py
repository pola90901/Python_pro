import os
os.system("echo hello terminal command ps should work")
y=os.popen("ps")#excute ps command
y=y.read()
print(y)

