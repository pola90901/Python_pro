import os
os.system("echo hello terminal command head  should work")
y=os.popen("head ")#excute head  command
y=y.read()
print(y)

