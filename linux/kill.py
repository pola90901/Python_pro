import os
os.system("echo hello terminal command kill should work")
y=os.popen("kill")#excute kill command
y=y.read()
print(y)

