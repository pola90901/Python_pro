import os
os.system("echo hello terminal command su should work")
y=os.popen("su")#excute su command
y=y.read()
print(y)

