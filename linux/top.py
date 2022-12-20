import os
os.system("echo hello terminal command top should work")
y=os.popen("top")#excute top command
y=y.read()
print(y)

