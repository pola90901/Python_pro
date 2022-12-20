import os
os.system("echo hello terminal command vi should work")
y=os.popen("vi")#excute vi command
y=y.read()
print(y)

