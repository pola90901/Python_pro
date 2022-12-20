import os
os.system("echo hello terminal command pwd should work")
y=os.popen("pwd")#excute pwd command
y=y.read()
print(y)

