import os
os.system("echo hello terminal command unzip should work")
y=os.popen("unzip")#excute unzip command
y=y.read()
print(y)

