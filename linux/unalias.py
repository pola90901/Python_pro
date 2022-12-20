import os
os.system("echo hello terminal command unalias should work")
y=os.popen("unalias")#excute unalias command
y=y.read()
print(y)

